from logging import FileHandler, Formatter, StreamHandler

from flask import Flask
from flask.logging import default_handler


def setup_loggers(app: Flask):
    """Configura os loggers para a aplicação"""
    formater = Formatter(
        fmt="[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        datefmt="%d-%m-%Y,%H:%M:%S",
    )
    # file handler
    file_handler = FileHandler(app.config["LOG_FILE"])
    file_handler.setFormatter(formater)
    # stream handler
    stream_handler = StreamHandler()
    stream_handler.setFormatter(formater)
    # add handlers
    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)
    # remover default handler
    app.logger.removeHandler(default_handler)
    return app
