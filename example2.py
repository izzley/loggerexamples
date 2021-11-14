from logconfig import logconfig
import logging

logger = logging.getLogger('anotherone')
logger.setLevel(logging.INFO)
logger.info("test")

loglogger = logging.getLogger('logconfig')
loglogger.setLevel(logging.INFO)
loglogger.info("Did anthing run?")
import example1

