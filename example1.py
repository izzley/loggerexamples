from logconfig import logconfig
import logging

print(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
print(logger.parent)
logger.info("Running Example1.py")