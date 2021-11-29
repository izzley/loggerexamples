"""
Read conf.YAML and setting up filter classes. 
This info is parsed to src/logconfig/__init__.py
"""

import logging
import logging.config
from pathlib import Path

import yaml


class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO


class DebugFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG


class WarnFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING


class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR


class CriticalFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.CRITICAL


def setup_logging():
    p = Path("src/logconfig/conf.yaml")
    with open(p, "r") as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)
    return None
