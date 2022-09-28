# from crypt import methods
from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of war', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nick, senha):
        self.nome = nome
        self.nick = nick
        self.senha = senha

usuario1 = Usuario('Rafael Paim', 'rafa', 'senha123')
usuario2 = Usuario('Daiane Cardoso', 'daiane', 'senha123')

usuarios = {usuario1.nick : usuario1,
            usuario2.nick : usuario2}

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/') # Criando uma rota
def index():
    
    return render_template('lista.html', titulo='Jogos', jogos=lista)  

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nick
            flash(usuario.nick+' logado com sucesso') # Fazer uma função para alertar a mensagem
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Falha no login')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout')
    return redirect(url_for('index'))

app.run(debug=True, host='0.0.0.0', port=3030) # ou app.run() somente
# Se eu quiser usar a porta 8080 para aplicação ou até mesmo 
# permitir acessos externos à aplicação definindo o host como 0.0.0.0