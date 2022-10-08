# from crypt import methods
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from views_game import *
from views_user import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3030) # ou app.run() somente
    # Se eu quiser usar a porta 8080 para aplicação ou até mesmo 
    # permitir acessos externos à aplicação definindo o host como 0.0.0.0