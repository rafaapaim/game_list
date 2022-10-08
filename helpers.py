import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.data_required(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.data_required(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.data_required(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nick = StringField('Nick', [validators.data_required(), validators.Length(min=1, max=8)])
    senha= PasswordField('Senha', [validators.data_required(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']): # Listando todos os arquivos do diretorio com a função os.listdir
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa-padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa-padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))