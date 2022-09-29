# from crypt import methods
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3030) # ou app.run() somente
    # Se eu quiser usar a porta 8080 para aplicação ou até mesmo 
    # permitir acessos externos à aplicação definindo o host como 0.0.0.0