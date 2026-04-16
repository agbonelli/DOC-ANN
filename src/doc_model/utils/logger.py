import logging
import sys
import os
from datetime import datetime

def setup_logger(config):
    level = getattr(logging, config["logging"]["level"])

    logger = logging.getLogger("doc_model")

    if logger.hasHandlers():
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] - %(message)s"
    )

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if config["logging"]["save_to_file"]:
        log_dir = config["logging"]["log_dir"]
        os.makedirs(log_dir, exist_ok=True)

        filename = datetime.now().strftime("run_%Y%m%d_%H%M%S.log")
        fh = logging.FileHandler(os.path.join(log_dir, filename))
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
