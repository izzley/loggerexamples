import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)
logger.warn("Running from logconfig/__init__.py: set to Warn")

# not sure why output is text only
logger.critical("Critical test")