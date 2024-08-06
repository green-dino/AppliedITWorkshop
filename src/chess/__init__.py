# __init__.py

# Package Metadata
__author__ = "Rye"
__email__ = "rye@grcand.me"
__version__ = "0.1.0"
__description__ = "a simple beautiful soup script"

# Logging Configuration 
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Package initialized successfully")