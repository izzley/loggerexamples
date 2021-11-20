# from logconfig import logconfig # The root logger does not need to be imported each time IF the root logger (i.e logconfig.logconfig) has been called from main
import logging
logger = logging.getLogger(__name__)
logger.info("Running Example1.py")

CONST = 122000

def proofofconcept():
    # Function does something
    logger.info(f"This Func outputs a CONST: {CONST}")
    return None

logger.debug(proofofconcept())

def funccalc():
    logger.debug("another thing")
    a = 1 + 1
    return a
    
# loggers can output function values too
logger.info(funccalc())