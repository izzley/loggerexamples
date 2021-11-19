import logging
import logging.config
import yaml

class infoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG

def setuplogging():
    with open('logconfig/config01.YAML', 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)
