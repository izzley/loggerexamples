"""
This module is the main file where all other modules are called into

"""

import logging

import module01
# setuplogging function called from __init__.py implicitly
from logconfig import logconfig

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # example set to DEBUG i.e all message below will print

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

# loggers can output function values too

module01.proofofconcept()

module01.funccalc(100000000)

