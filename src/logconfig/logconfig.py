import logging
import logging.config
from pathlib import Path

import yaml


class infoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

class debugFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG

class warnFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING

class errorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

class criticalFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.CRITICAL

def setuplogging():
    p = Path('src/logconfig/conf.YAML')
    with open(p, 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)
