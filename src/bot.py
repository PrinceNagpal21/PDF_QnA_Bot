import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Get Slack token from environment variables
try:
    slack_token = os.environ["SLACK_TOKEN"]
except KeyError:
    logger.error("SLACK_TOKEN not found in environment variables.")
    raise

# Initialize Slack client
client = slack.WebClient(token=slack_token)

logger.info("Slack client initialized successfully.")
