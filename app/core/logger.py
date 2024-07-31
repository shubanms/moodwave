import logging


def create_logger(name: str, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.setLevel(level)

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
    )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


logger = create_logger(__name__)
