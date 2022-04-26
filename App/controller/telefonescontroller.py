from app import app
from flask import render_template, request, flash, redirect, url_for
from model.telefonesmodel import Telefone, db
from model.pessoasmodel import Pessoa
from model.proprietariosmodel import *
from model.inquilinosmodel import *
from model.corretoresmodel import *


def telefonePrimeiroCadastro(telefone):
    db.session.add(telefone)
    db.session.commit()
    
def deletarListaTelefones(pessoaId):
    telefones = Telefone.query.filter_by(id_pessoa=pessoaId)
    for telefone in telefones:
        db.session.delete(telefone)
    db.session.commit()
                
@app.route("/inquilino/<int:inquilinoId>/telefones")
def listaTelefonesInquilino(inquilinoId):
    inquilino = Inquilino.query.filter_by(id=inquilinoId).first()    
    cpf = inquilino.cpf
    pessoa = Pessoa.query.filter_by(documento = cpf).first()
    pessoaId = pessoa.id
    telefones = Telefone.query.filter_by(id_pessoa=pessoaId)
    return render_template("listatelefonesInquilinos.html", telefones = telefones, pessoa = pessoa, pessoaId = pessoaId)


@app.route("/proprietario/<int:proprietarioId>/telefones")
def listaTelefonesProprietario(proprietarioId):
    proprietario = Proprietario.query.filter_by(id=proprietarioId).first()
    cpf = proprietario.cpf
    pessoa = Pessoa.query.filter_by(documento = cpf).first()
    pessoaId = pessoa.id
    telefones = Telefone.query.filter_by(id_pessoa=pessoaId)
    return render_template("listatelefonesproprietarios.html", telefones = telefones, pessoa = pessoa, pessoaId = pessoaId)

@app.route("/corretor/<int:corretorId>/telefones")
def listaTelefonesCorretor(corretorId):
    corretor = Corretor.query.filter_by(id=corretorId).first()
    matricula = corretor.matricula
    pessoa = Pessoa.query.filter_by(documento = matricula).first()
    pessoaId = pessoa.id
    telefones = Telefone.query.filter_by(id_pessoa=pessoaId)
    return render_template("listatelefonescorretores.html", telefones = telefones, pessoa = pessoa, pessoaId = pessoaId)
    
@app.route("/pessoa/<int:pessoaId>/telefones/cadastro")
def cadastroTelefones(pessoaId):
    return render_template("cadastrotelefones.html", pessoaId = pessoaId)

@app.route("/pessoa/<int:pessoaId>/telefones/cadastrar", methods=['GET', 'POST'])
def cadastrarTelefones(pessoaId):
    if request.method == "POST":
        if not request.form['ddd'] or not request.form['numero'] or not request.form['contato']:
             flash('Preencha todos os campos!', 'Erro!')
        else:        
            telefone = Telefone(request.form['ddd'], request.form['numero'], request.form['contato'], pessoaId)                 
            db.session.add(telefone)        
            db.session.commit()                                        
            flash('Telefone Adicionado Com Sucesso!')
    return redirect(url_for("index"))

@app.route("/telefones/deletar/<int:id>")
def deletarTelefones(id):
    telefone = Telefone.query.filter_by(id=id).first()    
    db.session.delete(telefone)
    db.session.commit()            
    return redirect(url_for("index"))

@app.route("/telefones/atualizar/<int:id>", methods=['GET', 'POST'])    
def atualizarTelefones(id):
    telefone = Telefone.query.filter_by(id=id).first()
    if request.method == "POST":
        ddd = request.form.get("ddd")        
        numero = request.form.get("numero")
        contato = request.form.get("contato")
        pessoaId = telefone.id_pessoa
        if ddd and numero and contato:            
            telefone.ddd = ddd
            telefone.numero = numero
            telefone.contato = contato                        
            telefone.id_pessoa = pessoaId
            db.session.commit()                        
            return redirect(url_for("index"))
    return render_template("atualizartelefones.html", telefone=telefone)        
