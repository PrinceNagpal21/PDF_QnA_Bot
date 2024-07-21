# PDF_QnA_Bot

# Zania AI Assistant

This repository contains the code for Zania's Employee AI Assistant. The assistant is built using various Python libraries, including Streamlit, PyPDF2, Langchain, and OpenAI embeddings, among others. It allows users to upload PDF files, extract text, split it into chunks, vectorize the chunks, and perform question-answering based on the extracted content.

## Features

- Extract text from PDF documents.
- Split text into manageable chunks.
- Vectorize text chunks using OpenAI embeddings.
- Save vectorized text chunks using FAISS.
- Answer questions based on the provided PDF content using a conversational chain.

## Requirements

- Python 3.8 or higher
- Streamlit
- PyPDF2
- langchain-community
- openai
- slack-sdk
- python-dotenv

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/zania-ai-assistant.git
    cd zania-ai-assistant
    ```

2. Create and activate a virtual environment:

    ```
    python -m ven venv
    conda activate venv 
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory.
    - Add the following environment variables to the `.env` file:

    ```env
    SLACK_TOKEN=your-slack-token
    OPENAI_API_KEY=your-openai-api-key
    ```

5. Create a `config` directory in the root directory and add the config file with name `app_config.yaml`.

## Usage

1. Run the Streamlit app:

    ```
    streamlit run app.py
    ```

2. Upload your PDF files using the sidebar menu in the Streamlit app.
3. Ask questions based on the content of the uploaded PDFs.
