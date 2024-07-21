from PyPDF2 import PdfReader
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_pdf_text(pdf_docs):
    """
    Extract text from a list of PDF documents.

    Args:
        pdf_docs (list): List of PDF file paths or file-like objects.

    Returns:
        str: The extracted text from all provided PDF documents.
    """
    logger.info("Starting to extract text from PDF documents.")
    text = ""
    
    # Iterate through each PDF document
    for pdf in pdf_docs:
        logger.info("Processing PDF: %s", pdf)
        try:
            pdf_reader = PdfReader(pdf)
            
            # Extract text from each page of the PDF
            for page in pdf_reader.pages:
                text += page.extract_text()
            logger.info("Extracted text from %d pages.", len(pdf_reader.pages))
        except Exception as e:
            logger.error("Error processing PDF %s: %s", pdf, e)
    
    logger.info("Finished extracting text from all PDF documents.")
    return text
