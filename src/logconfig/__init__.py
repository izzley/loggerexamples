"""
This module calls the setuplogging function and creates a root logger instance.
All future loggers will inherit these yaml configurations from this root logger.
Python uses __init__.py files to navigate between folders. They are implicitly executed.
"""
import logging
from logconfig.logconfig import setup_logging
from pathlib import Path

# make sure logfiles/ directory exists
p = Path.cwd() / "src/logfiles"
if not p.exists():
    Path.mkdir(p)

# setuplogging function called from logconfig.py
setup_logging()

logger = logging.getLogger(__name__)

logger.info("Root logger setup successful")