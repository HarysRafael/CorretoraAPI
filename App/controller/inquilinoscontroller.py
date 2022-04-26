from app import app
from controller.telefonescontroller import telefonePrimeiroCadastro
from flask import render_template, request, redirect, url_for, flash
from model.inquilinosmodel import Inquilino, db
from model.telefonesmodel import Telefone
from model.pessoasmodel import *
from controller.pessoascontroller import *

#Arquivo com rotas relacionadas ao CRUD da entidade Inquilinos

@app.route("/inquilinos")
def inquilinos():
    return render_template("inquilinos.html")

@app.route("/inquilinos/cadastro")
def cadastroInquilinos():
    return render_template("cadastroinquilinos.html")

@app.route("/inquilinos/cadastrar", methods=['GET', 'POST'])
def cadastrarInquilinos():
    if not request.form['nome'] or not request.form['cpf'] or not request.form['email'] or not request.form['ddd'] or not request.form['numero'] or not request.form['contato']:
         flash('Preencha todos os campos!', 'Erro!')
    else:
        
        inquilino = Inquilino(request.form['nome'], request.form['cpf'], request.form['email'])
        db.session.add(inquilino)
        db.session.commit()  
        pessoa = Pessoa(inquilino.cpf)
        cadastrarPessoa(pessoa)
        pessoaTel = Pessoa.query.filter_by(documento=inquilino.cpf).first()
        telefone = Telefone(request.form['ddd'], request.form['numero'], request.form['contato'], pessoaTel.id)
        telefonePrimeiroCadastro(telefone)
                        
        flash('Inquilino Adicionado Com Sucesso!')    
    return redirect(url_for("inquilinos"))

@app.route("/inquilinos/deletar/<int:id>")
def deletarInquilinos(id):
    inquilino = Inquilino.query.filter_by(id=id).first()
    cpf = inquilino.cpf
    deletarPessoa(cpf)
    db.session.delete(inquilino)    
    db.session.commit()    
    inquilinos = Inquilino.query.all()
    return render_template("listainquilinos.html", inquilinos = inquilinos)
    
@app.route("/inquilinos/atualizar/<int:id>", methods=['GET', 'POST'])    
def atualizarInquilinos(id):
    inquilino = Inquilino.query.filter_by(id=id).first()
    if request.method == "POST":
        nome = request.form.get("nome")        
        email = request.form.get("email")                
        if nome and email:            
            inquilino.nome = nome
            inquilino.email = email            
            db.session.commit()            
            return redirect(url_for("listaInquilinos"))        
    return render_template("atualizarinquilinos.html", inquilino=inquilino)        
       
@app.route("/inquilinos/lista")    
def listaInquilinos():
    inquilinos = Inquilino.query.all()
    return render_template("listainquilinos.html", inquilinos = inquilinos)
