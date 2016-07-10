import logging

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__file__)
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)