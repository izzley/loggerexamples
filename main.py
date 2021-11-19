import logging

from logconfig.logconfig import setuplogging

setuplogging()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # example set to DEBUG i.e 

logger.debug("debugging stuff")
logger.debug("Detailed information, typically of interest only when diagnosing problems.")

logger.info("Well thats informative")
logger.info("Confirmation that things are working as expected.")

logger.warning("We're just warning up")
logger.warning("An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.")

logger.error("Erronius")
logger.error("Due to a more serious problem, the software has not been able to perform some function.")

logger.critical("Chaos ensues")
logger.critical("A serious error, indicating that the program itself may be unable to continue running.")

import example1

# print(devlogger.getChild())
