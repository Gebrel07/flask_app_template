# Template de aplicação Flask + MongoDb
Este é um esqueleto simples para iniciar um projeto Web App ou API usando o microframework Flask.

## Estrutura do projeto
```
├── src/
|   ├── main/
│   │   └── modulos/
│   ├── app.py
│   ├── blueprints.py
│   ├── configs.py
│   ├── error_handlers.py
│   ├── extensions.py
│   ├── loggers.py
├── test/
|   ├── conftest.py
|   └── testes.py
├── instance/
├── .env
├── .flaskenv
└── app.log
```

### main
Módulos que devem conter os endpoints e lógica do sistema.

Os endpoints de exemplo são organizados por meio de Blueprints como em src.main.routes.exemplo:
```python
exemplo_bp = Blueprint(name="exemplo", import_name=__name__, url_prefix=None)
```
Cada blueprint comporta multiplas routes.

### app.py
Gerador de instancia da aplicação. Cria objeto da aplicação e aplica as configurações determinadas pela classe de configuração escolhida.

Cria a aplicação através da função "create_app". As configurações da aplicação são definidas a partir do primeiro argumento da função, que deve ser um string contendo o caminho relativo da classe de configuração. Ex: 

```python
from src.app import create_app
app = create_app("src.configs.ConfigBase")
```

### blueprints.py
Registro de Blueprints (routes, endpoints) da aplicação. Importa as blueprints de seus respectivos módulos em "main" e as registra na aplicação.

### configs.py
Classes de configuração para a aplicação. Carregam as variáveis definidas para o ambiente e aplicam à aplicação durante sua inicialização.

Cada atributo das classes representa uma variável de ambiente necessária para a aplicação funcionar.

### error_handlers.py
Registro de error handlers gerais da aplicação. Capturam erros inesperados durante a execução e tratam de acordo com o tipo de erro e função definida.

### extensions.py
Extensões adicionadas à aplicação. Inicializa as extensões para serem acopladas à aplicação. Exemplo: flask_pymongo, flask_sqlalchemy, flask_jwt_extended etc...

### loggers.py
Registro de loggers da aplicação. Configura os loggers e acopla à aplicação durante sua inicialização. Registra output em app.log e stoud.

### conftest.py
Configurações gerais para os testes. Inicializa aplicação com configurações de teste e executa funções definidas (fixtures) antes de cada teste.

### instance
A pasta "instance" é uma caracteristica das versões mais atuais de Flask. Use-a para armazenar arquivos que são específicos ao ambiente que executa o projeto. Como por exemplo, uploads de arquivos, imagens de perfil de usuários etc...
**Esta pasta deve ser ignorada pelo controle de versionamento.**

## Váriaveis de ambiente
As configurações da aplicação, como URI do banco de dados chave de hash etc... São adiquiridas através das váriaveis de ambiente. Estas podem ser definidas manualmente, através do console, ou salvas nos arquivos definidos abaixo, na pasta raiz do projeto:
### .env
Váriaveis privadas. URI de banco de dados, credenciais etc. **Atenção: Exclua do controle de versionamento em projeto real**

### .flaskenv
Váriaveis públicas específicas de Flask. Contém prefixo FLASK_. Ex: FLASK_DEBUG = True. **Atenção: Exclua do controle de versionamento em projeto real**

## Iniciando a aplicação
Antes de iniciar a aplicação, tenha certeza de que as variáveis de ambiente necessárias foram definidas (via console ou através dos arquivos .env).

Acesse o terminal e execute esses comandos dentro da pasta raiz do projeto.
```bash
# criar ambiente virtual do projeto
python3 -m venv .venv

# ativar ambiente virtual
source .venv/bin/activate

# instalar dependencias do projeto
pip install -r requirements.txt

# iniciar aplicação
flask run
```
Isso iniciará a aplicação em modo de desenvolvimento.

**Atenção**: Esse modo não é recomendado para ambientes de produção. Nestes casos, é recomendado utilizar [Gunicorn](https://gunicorn.org/) + um servidor web de alta capacidade como [Nginx](https://www.nginx.com/)