import pytest

from src.app import create_app


@pytest.fixture()
def app():
    app = create_app("src.configs.ConfigTest")
    # não logar erros durante os testes
    app.logger.disabled = True
    yield app
