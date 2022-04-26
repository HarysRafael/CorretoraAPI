from app import app
from controller.telefonescontroller import telefonePrimeiroCadastro
from controller.pessoascontroller import *
from flask import render_template, request, redirect, url_for, flash
from model.corretoresmodel import Corretor, db
from model.telefonesmodel import Telefone

#Arquivo com rotas relacionadas ao CRUD de corretores

@app.route("/corretores")
def corretores():
    return render_template("corretores.html")

@app.route("/corretores/cadastro")
def cadastroCorretores():
    return render_template("cadastrocorretores.html")

@app.route("/corretores/cadastrar", methods=['GET', 'POST'])
def cadastrarCorretores():
    if not request.form['nome'] or not request.form['matricula'] or not request.form['email'] or not request.form['ddd'] or not request.form['numero'] or not request.form['contato']:
         flash('Preencha todos os campos!', 'Erro!')
    else:
        
        corretor = Corretor(request.form['nome'], request.form['matricula'], request.form['email'])
        pessoa = Pessoa(corretor.matricula)
        db.session.add(corretor)        
        db.session.commit()  
        cadastrarPessoa(pessoa)
        corretorTel = Pessoa.query.filter_by(documento=corretor.matricula).first()
        telefone = Telefone(request.form['ddd'], request.form['numero'], request.form['contato'], corretorTel.id)
        telefonePrimeiroCadastro(telefone)
                        
        flash('Corretor Adicionado Com Sucesso!')
    return redirect(url_for("corretores"))

@app.route("/corretores/deletar/<int:id>")
def deletarCorretores(id):
    corretor = Corretor.query.filter_by(id=id).first()    
    matricula = corretor.matricula
    deletarPessoa(matricula)
    db.session.delete(corretor)    
    db.session.commit()    
    corretores = Corretor.query.all()
    return render_template("listacorretores.html", corretores = corretores)
    
@app.route("/corretores/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizarCorretores(id):
    corretor = Corretor.query.filter_by(id=id).first()    
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        
        if nome and email:
            corretor.nome = nome
            corretor.email = email                                    
            db.session.commit()                                
            return redirect(url_for("listaCorretores"))
    return render_template("atualizarcorretores.html", corretor=corretor)

@app.route("/corretores/lista")
def listaCorretores():
    corretores = Corretor.query.all()
    return render_template("listacorretores.html", corretores = corretores)

