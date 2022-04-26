from controller.imoveiscontroller import deletarListaImoveis
from app import app
from controller.telefonescontroller import telefonePrimeiroCadastro
from controller.pessoascontroller import *
from flask import render_template, request, redirect, url_for, flash
from model.proprietariosmodel import Proprietario, db
from model.telefonesmodel import Telefone

#Arquivo com rotas relacionadas ao CRUD da entidade Proprietários

@app.route("/proprietarios")
def proprietarios():
    return render_template("proprietarios.html")

@app.route("/proprietarios/cadastro")
def cadastroProprietarios():
    return render_template("cadastroproprietarios.html")

@app.route("/proprietarios/cadastrar", methods=['GET', 'POST'])
def cadastrarProprietarios():
    if not request.form['nome'] or not request.form['cpf'] or not request.form['email'] or not request.form['ddd'] or not request.form['numero'] or not request.form['contato']:
         flash('Preencha todos os campos!', 'Erro!')
    else:        
        proprietario = Proprietario(request.form['nome'], request.form['cpf'], request.form['email'])
        pessoa = Pessoa(proprietario.cpf)
        db.session.add(proprietario)        
        db.session.commit()  
        cadastrarPessoa(pessoa)
        proprietarioTel = Pessoa.query.filter_by(documento=proprietario.cpf).first()
        telefone = Telefone(request.form['ddd'], request.form['numero'], request.form['contato'], proprietarioTel.id)
        telefonePrimeiroCadastro(telefone)
                        
        flash('Proprietário Adicionado Com Sucesso!')
        
    return render_template("proprietarios.html")

@app.route("/proprietarios/deletar/<int:id>")
def deletarProprietarios(id):
    proprietario = Proprietario.query.filter_by(id=id).first()    
    cpf = proprietario.cpf
    deletarPessoa(cpf)
    deletarListaImoveis(proprietario.id)
    db.session.delete(proprietario)    
    db.session.commit()    
    proprietarios = Proprietario.query.all()
    return render_template("listaproprietarios.html", proprietarios = proprietarios)
    
@app.route("/proprietarios/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizarProprietarios(id):
    proprietario = Proprietario.query.filter_by(id=id).first()    
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        
        if nome and email:
            proprietario.nome = nome
            proprietario.email = email                                    
            db.session.commit()                                
            return redirect(url_for("listaProprietarios"))
    return render_template("atualizarproprietarios.html", proprietario=proprietario)

@app.route("/proprietarios/lista")
def listaProprietarios():
    proprietarios = Proprietario.query.all()
    return render_template("listaproprietarios.html", proprietarios = proprietarios)

