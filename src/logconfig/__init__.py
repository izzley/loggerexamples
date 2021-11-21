# __init__.py files are interesting. Python.exe uses them to navigated folders hence they are implicitly called/run.
# Below setup function is called implicitly from main
import logging
from logconfig.logconfig import setuplogging
from pathlib import Path

# make sure logfiles/ directory exists
p = Path.cwd() / "src/logfiles"
if not p.exists():
    Path.mkdir(p)

# setuplogging function called from logconfig.py
setuplogging()

logger = logging.getLogger(__name__)

logger.info("Root logger setup successful")