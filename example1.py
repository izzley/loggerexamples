# from logconfig import logconfig # The root logger does not need to be imported each time IF the root logger (i.e logconfig.logconfig) has been called from main
import logging
logger = logging.getLogger(__name__)
logger.info("Running Example1.py")

Bigone = 122000

def running():
    # did something
    logger.info(f"yeeeaaah. Look at the func with this Bigone: {Bigone}")
    return None

running()