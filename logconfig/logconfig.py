import logging
import logging.config
import yaml

class infoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO

def setuplogging():
    with open('logconfig/config01.YAML', 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        logging.config.dictConfig(log_cfg)
