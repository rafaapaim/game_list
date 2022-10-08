from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nick=form.nick.data).first() # (nick=request.form['usuario']).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        #if form.senha.data == usuario.senha: # request.form['senha']
        session['usuario_logado'] = usuario.nick
        flash(usuario.nick + ' logado com sucesso')
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
