from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_text_chunks(text):
    """
    Split the given text into chunks using RecursiveCharacterTextSplitter.
    
    Args:
        text (str): The input text to be split into chunks.
    
    Returns:
        list: A list of text chunks.
    """
    logger.info("Starting to split the text into chunks.")
    
    # Initialize text splitter with specified chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    
    # Split the text into chunks
    chunks = text_splitter.split_text(text)
    
    logger.info("Text split into %d chunks.", len(chunks))
    
    return chunks
