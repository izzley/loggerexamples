import logging
import logging.config

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
    with open('logconfig/config01.YAML', 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)
