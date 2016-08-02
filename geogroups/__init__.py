import logging

logger = logging.getLogger(__file__)


def configure(settings):
    logging.basicConfig(format=settings.LOG_FORMAT)
    if settings.DEBUG:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
