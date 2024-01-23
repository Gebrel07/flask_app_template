from flask import Flask

from .main.routes_exemplo import exemplo_bp


def registrar_blueprints(app: Flask):
    """Registra todas as Blueprints no app passado"""
    app.register_blueprint(exemplo_bp)
    return app
