import logging

from fastapi import FastAPI

from app.core.config import settings

from app.core.device import DEVICE

from app.core.logging_config import (
    configure_logging
)

from app.core.container import (
    container
)


configure_logging()


logger = logging.getLogger(
    "anpr"
)


app = FastAPI(

    title=settings.app_name,

    version="1.0.0"
)


@app.get("/")
def root():

    return {

        "application":
            settings.app_name,

        "environment":
            settings.app_env,

        "device":
            DEVICE,

        "status":
            "running"
    }


@app.get("/health")
def health():

    return {

        "status":
            "healthy",

        "device":
            DEVICE,

        "sessions":
            len(
                container.sessions.all()
            )
    }