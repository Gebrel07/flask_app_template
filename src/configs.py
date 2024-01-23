import os
from typing import Any

from dotenv import load_dotenv


class ConfigBase:
    def __init__(self) -> None:
        # ler arquivos de ambiente (se houver) e carregar suas variaveis no ambiente
        load_dotenv(dotenv_path=".flaskenv", override=True)
        load_dotenv(dotenv_path=".env", override=True)
        # chaves de configuração
        self.SECRET_KEY = self.get_env_var(key="SECRET_KEY")
        self.MONGO_URI = self.get_env_var(key="MONGO_URI")
        self.LOG_FILE = self.get_env_var(key="LOG_FILE")

    def get_env_var(self, key: str) -> Any:
        """Adquirir valor de uma variavel de ambiente"""
        val = os.getenv(key=key)
        if val is None:
            raise ValueError(f"Variável {key} não encontrada no ambiente")
        if val == "True":
            return True
        if val == "False":
            return False
        if "," in val:
            return val.replace(" ", "").split(sep=",")
        if val.isnumeric():
            return int(val)
        return val


class ConfigTest(ConfigBase):
    def __init__(self) -> None:
        super().__init__()
        self.SECRET_KEY = self.get_env_var(key="SECRET_KEY_TEST")
        self.MONGO_URI = self.get_env_var(key="MONGO_URI_TEST")
