from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

import os
import yaml
from dotenv import load_dotenv
from pathlib import Path
import logging

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

embedding_model = app_config["Model"]["embedding_model"]

def get_vector_store(text_chunks):
    """
    Create a FAISS vector store from text chunks using OpenAI embeddings and save it locally.

    Args:
        text_chunks (list): A list of text chunks to be vectorized and stored.

    Returns:
        None
    """
    logger.info("Starting to create vector store from text chunks.")
    
    try:
        # Initialize embeddings model
        embeddings = OpenAIEmbeddings(model=embedding_model)
        
        # Create FAISS vector store from text chunks
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        
        # Save the vector store locally
        vector_store.save_local("faiss_index")
        
        logger.info("Vector store created and saved successfully.")
    except Exception as e:
        logger.error("Error creating vector store: %s", e)
        raise

