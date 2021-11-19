import logging

from logconfig.logconfig import setuplogging

setuplogging()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info("test")

logger.debug("debugging stuff")

loglogger = logging.getLogger('logconfig')
loglogger.setLevel(logging.INFO)
loglogger.info("Did anthing run?")

# devlogger level is set to DEBUG and the dev logger is configured to write to debug.log
devlogger = logging.getLogger('dev')
devlogger.setLevel(logging.DEBUG)
devlogger.info("devLogger")

devlogger.warning("We're just warning up")
devlogger.critical("Whoa critical error")

import example1

# print(devlogger.getChild())
