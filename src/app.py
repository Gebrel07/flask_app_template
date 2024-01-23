from flask import Flask
from werkzeug.utils import import_string

from .blueprints import registrar_blueprints
from .error_handlers import registar_error_handlers
from .extensions import mongo
from .loggers import setup_loggers


def create_app(config_cls: str):
    """Criar aplicação utilizando as configurações da classe passada.

    Args:
        config_cls (str): caminho relativo de importação da
        classe de configuração. Ex: 'src.configs.ConfigTeste'
    """
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
    )
    # configurar app a partir de objeto
    conf = import_string(config_cls)()
    app.config.from_object(obj=conf)
    # configurar loggers
    app = setup_loggers(app)
    # log exemplo
    app.logger.info(f"App started with config mode: {type(conf).__name__}")
    # extensoes
    mongo.init_app(app=app)
    # registrar routes
    app = registrar_blueprints(app)
    # error handlers
    app = registar_error_handlers(app)
    return app
