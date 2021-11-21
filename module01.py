# from logconfig import logconfig # The root logger does not need to be imported each time IF the root logger (i.e logconfig.logconfig) has been called from main
import logging
from utils.timefunction import timing
logger = logging.getLogger(__name__)
logger.info("Running Example1.py")

CONST = 122000

@timing
def proofofconcept():
    # Function does something
    logger.info(f"This Func outputs a CONST: {CONST}")
    return None

@timing
def funccalc(n):
    logger.debug("another thing")
    for _ in range(n):
        i = 0
    return