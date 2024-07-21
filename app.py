import yaml
from dotenv import load_dotenv
from pathlib import Path
import os
import streamlit as st
import logging
from src import bot
from src.chunks import get_text_chunks
from src.read_pdf import get_pdf_text
from src.vectorization import get_vector_store
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
os.chdir("D:/Zania")
config_path = "config/"

# Load configuration file
with open(config_path + "app_config.yaml", "r") as f:
    app_config = yaml.load(f, Loader=yaml.SafeLoader)

# Extract configuration details
embedding_model = app_config["Model"]["embedding_model"]
modelling = app_config["Model"]["model"]
temperature = app_config["Model"]["temperature"]

system_role = app_config["Prompts"]["system_role"]
guidelines = app_config["Prompts"]["guidelines"]
examples = app_config["Prompts"]["examples"]

def get_conversational_chain():
    """
    Create a conversational chain for question answering based on the provided guidelines and examples.

    Returns:
        chain (Chain): A question-answering chain with the specified prompt template.
    """
    prompt_template = f"""
    \n {system_role}\n

    \n {guidelines}\n

    \n {examples}\n

    Begin answering questions according to these guidelines and the examples."""
    prompt_template = prompt_template + """
    Context:\n {context} \n

    Question: \n {question} \n

    Answer:
    """
    model = ChatOpenAI(model=modelling, temperature=temperature)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "questions"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    """
    Process the user's input question and generate a response using the conversational chain.

    Args:
        user_question (str): The question asked by the user.
    """
    embeddings = OpenAIEmbeddings(model=embedding_model)
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

    bot.client.chat_postMessage(channel="test", text={"question": user_question, "answer": response["output_text"]})
    st.write("Response: ", {"question": user_question, "answer": response["output_text"]})

def main():
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config("Chat PDF")
    st.header("Chat with Zania's Employee AI assistant")

    user_question = st.text_input("Ask a Question from the PDF Files")
    st.markdown("<p style='font-size: smaller;'>Please separate the question with commas</p>", unsafe_allow_html=True)
    if user_question:
        for question in user_question.split(","):
            user_input(question)

    with st.sidebar:
        st.title("Menu: ")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button",
                                    accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    logger.info("Starting the Streamlit app")
    main()
