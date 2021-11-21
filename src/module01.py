"""
This is an example of a first party module (written by you) using logging messages and the timing decorator
"""
import logging
from utils.timefunction import timing

# If this file is not run from mainmodule.py, the root logger is not configured yet from src/logconfig.
if __name__ == "__main__":
    from logconfig import logconfig

logger = logging.getLogger(__name__)
logger.info("Running module01.py")

CONST = 122000

@timing
def proofofconcept():
    """
    Loggers can run from anywhere including within funcs
    """
    logger.info(f"This Func outputs a CONST: {CONST}")
    return None

@timing
def funccalc(n):
    """
    Take a look at the start and finish times in the console or logfiles/root.log
    """
    logger.warning("started")
    for _ in range(n):
        i = 0
    logger.warning("finished")
    return


if __name__ == "__main__":
    funccalc(100000000)