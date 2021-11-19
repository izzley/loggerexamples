# from logconfig import logconfig # The root logger does not need to be imported each time IF the root logger (i.e logconfig.logconfig) has been called from main
import logging

print(__name__)

logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# print(logger.parent)
logger.info("Running Example1.py")

def running():
    # did something
    logger.info("yeeeaaah. Look at the func")
    return None

running()