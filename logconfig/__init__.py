# __init__.py files are interesting. Python.exe uses them to navigated folders hence they are implicitly called/run.
# Below setup function is called implicitly from main
import logging
from os import mkdir
from logconfig.logconfig import setuplogging
from pathlib import Path

# make sure logfiles/ directory exists
if not (Path.cwd() / "logfiles").exists():
    Path.mkdir(Path.cwd() / "logfiles")

# take a look at logconfig.py
setuplogging()

logger = logging.getLogger(__name__)

logger.info("Root logger setup successful")