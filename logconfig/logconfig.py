import logging
import logging.config
import yaml

with open('logconfig/config01.YAML', 'r') as f:

    log_cfg = yaml.safe_load(f.read())

logging.config.dictConfig(log_cfg)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('This is an info message')
logger.error('This is an error message')