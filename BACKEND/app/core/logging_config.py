import logging
import sys

from pathlib import Path

from app.core.config import settings


def configure_logging():

    log_file = (
        settings.log_path /
        "anpr.log"
    )

    formatter = logging.Formatter(

        "%(asctime)s "
        "%(levelname)s "
        "%(name)s | "
        "%(message)s"
    )


    # ----------------------------------
    # Console
    # ----------------------------------

    console_handler = (
        logging.StreamHandler(sys.stdout)
    )

    console_handler.setFormatter(
        formatter
    )


    # ----------------------------------
    # File
    # ----------------------------------

    file_handler = (
        logging.FileHandler(
            log_file,
            encoding="utf-8"
        )
    )

    file_handler.setFormatter(
        formatter
    )


    # ----------------------------------
    # Root logger
    # ----------------------------------

    root_logger = logging.getLogger()

    root_logger.setLevel(
        logging.INFO
    )

    root_logger.handlers.clear()

    root_logger.addHandler(
        console_handler
    )

    root_logger.addHandler(
        file_handler
    )