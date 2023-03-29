from loguru import logger
import sys


class file_info:
    def __init__(self):
        logger.remove()
        self.configuration_format()
        self.configuration_logger()

    def configuration_format(self):
        self.FORMAT_WARNING = "{time:YYYY-MM-DD HH:mm} | {level} | {message}"
        self.FORMAT_WARNING_CLI = (
            "{level.icon} {time:YYYY-MM-DD HH:mm} | {level} | {message}"
        )
        self.FORMAT_SUCCESS = (
            "{time:YYYY-MM-DD HH:mm} | {level} | {function}| {message} "
        )
        self.FORMAT_INFO = "{time:YYYY-MM-DD HH:mm} | {level} | {message}"

    def configuration_logger(self):
        config = {
            "handlers": [
                {
                    "sink": sys.stderr,
                    "format": self.FORMAT_INFO,
                    "filter": lambda record: record["function"] == "info",
                },
                {
                    "sink": "logs/logs_{time:DD-MM-YYYY}.log",
                    "format": self.FORMAT_INFO,
                    "filter": lambda record: record["function"] == "info",
                },
                {
                    "sink": "logs/logs_{time:DD-MM-YYYY}.log",
                    "format": self.FORMAT_SUCCESS,
                    "filter": lambda record: record["function"] == "success",
                },
                {
                    "sink": "logs/logs_{time:DD-MM-YYYY}.log",
                    "format": self.FORMAT_WARNING,
                    "filter": lambda record: record["function"] == "warning",
                },
                {
                    "sink": sys.stderr,
                    "format": self.FORMAT_WARNING_CLI,
                    "filter": lambda record: record["function"] == "warning",
                },
            ],
            "levels": [{"name": "RESULT", "no": 38, "icon": "¤", "color": "<yellow>"}],
        }  # TODO Suite dev mise en place fichier result de comande switch.
        logger.configure(**config)

    def info(self, message):
        return logger.info(message)

    def success(self, message):
        return logger.success(message)

    def warning(self, message):
        return logger.warning(message)
