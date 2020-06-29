import logging
from config import EnvConfig

env = EnvConfig()


logging.basicConfig(
    level=env.log_level,
    format='%(asctime)s: [%(levelname)]-8s %(name)-15s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def get_logger(name):
    logger = logging.getLogger(name)

    return logger
