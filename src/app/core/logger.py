import logging.config
import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app.log")


LOGGER_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {},
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "%(asctime)s %(levelname)s %(name)s %(message)s",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "json",
            "filename": LOG_FILE,
            "when": "midnight",
            "backupCount": 7,
            "interval": 1,
            "encoding": "utf-8",
            "delay": False,
            "utc": False
        },
    },
    "loggers": {
        "app": {
            "level": "INFO",
            "handlers": ["stdout", "file"],
            "propagate": False,
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["stdout", "file"],
    }
}

logging.config.dictConfig(config=LOGGER_CONFIG)
logger = logging.getLogger("app")
