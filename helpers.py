import os
from jogoteca import app

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']): # Listando todos os arquivos do diretorio com a função os.listdir
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa-padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa-padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))