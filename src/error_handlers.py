from flask import Flask, current_app


def erro_geral(e):
    current_app.log_exception(e)
    return "Houve um erro interno", 500


def registar_error_handlers(app: Flask):
    """Registra error handlers no app passado"""
    app.register_error_handler(Exception, erro_geral)
    return app
