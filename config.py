import os

SECRET_KEY = 'chave_secreta'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector', # Sistema Gerenciador de Banco de Dados
        usuario = 'root',
        senha = '91022724',
        servidor = 'localhost',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'