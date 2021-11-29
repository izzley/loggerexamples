"""
This module is the main file where all other modules are called from.
This repo is designed to run from this file.
"""
import logging
from logconfig import logconfig # setuplogging function called from src/logconfig/__init__.py implicitly
# @TODO: Get RichHandler happening. https://rich.readthedocs.io/en/stable/logging.html
# from rich.logging import RichHandler
import other_module

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # example set to DEBUG i.e all message set to debug or higher output something

logger.debug("I deem this a bug... (squish)")
logger.debug("DEBUG: Detailed information, typically of interest only when diagnosing problems.")

logger.info("Well, good sir, thats informative")
logger.info("INFO: Confirmation that things are working as expected.")

logger.warning("We're just warning up")
logger.warning("WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.")

logger.error("Erronius")
logger.error("ERROR: Due to a more serious problem, the software has not been able to perform some function.")

logger.critical("Chaos ensues")
logger.critical("CRITICAL: A serious error, indicating that the program itself may be unable to continue running.")

# module01 functions called with loggers in them
other_module.proof_concept()
other_module.func_calc(100000000)

# logger.debug("End of the line", stack_info=True)
