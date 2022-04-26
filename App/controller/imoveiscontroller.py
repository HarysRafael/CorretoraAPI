from app import app
from flask import render_template, request, flash
from model.imoveismodel import Imovel, db
from random import random

#Arquivo criado com Rotas referente ao CRUD das entidades Imóveis e Endereços

@app.route("/imoveis")
def imoveis():
    return render_template("imoveis.html")

@app.route("/proprietario/<int:idProprietario>/imoveis")
def imoveisProprietario(idProprietario):
    return render_template("imoveisproprietario.html", idProprietario = idProprietario)

@app.route("/proprietario/<int:idProprietario>/listaimoveis")
def listaImoveisProprietario(idProprietario):
    imoveis = Imovel.query.filter_by(proprietario_id=idProprietario)
    return render_template("listaimoveisproprietario.html", imoveis = imoveis, idProprietario = idProprietario)

def deletarListaImoveis(idProprietario):
    imoveis = Imovel.query.filter_by(proprietario_id=idProprietario)
    for imovel in imoveis:              
        db.session.delete(imovel) 
    db.session.commit()
    
@app.route("/proprietario/<int:idProprietario>/cadastroimovel")
def cadastroImoveis(idProprietario):
    return render_template("cadastroimoveis.html", idProprietario = idProprietario)

@app.route("/proprietario/<int:idProprietario>/cadastrarimovel", methods=['GET', 'POST'])
def cadastrarImoveis(idProprietario):
    if request.method == "POST":   
        if not request.form['area'] or not request.form['preco'] or not request.form['tipo'] or not request.form['rua'] or not request.form['numero'] or not request.form['complemento'] or not request.form['bairro'] or not request.form['cidade'] or not request.form['cep']:
            flash('Preencha todos os campos!', 'Erro!')
        else:            
            imovel = Imovel(request.form['area'], request.form['preco'], request.form['tipo'], False, idProprietario, request.form['rua'], request.form['numero'], request.form['complemento'], request.form['bairro'], request.form['cidade'], request.form['cep'])
            db.session.add(imovel)        
            db.session.commit()                                        
            flash('Imóvel Adicionado Com Sucesso!')
            imoveis = Imovel.query.filter_by(proprietario_id=idProprietario)
            return render_template("listaimoveisproprietario.html", imoveis = imoveis, idProprietario = idProprietario)
                        

@app.route("/imovel/<int:id>/deletar")
def deletarImoveis(id):
    imovel = Imovel.query.filter_by(id=id).first()
    idProprietario = imovel.proprietario_id
    imoveis = Imovel.query.filter_by(proprietario_id=idProprietario)
    db.session.delete(imovel)
    db.session.commit()        
    return render_template("listaimoveisproprietario.html", imoveis = imoveis, idProprietario = idProprietario)
    
@app.route("/imovel/<int:id>/atualizar", methods=['GET', 'POST'])
def atualizarImoveis(id):
    imovel = Imovel.query.filter_by(id=id).first()        
    if request.method == "POST":
        area = request.form.get("area")
        preco = request.form.get("preco")
        tipo = request.form.get("tipo")
        rua = request.form.get("rua")
                
        if area and preco and tipo:            
            imovel.area = area
            imovel.preco = preco
            imovel.tipo = tipo                     
            imovel.rua = rua
            db.session.commit()                                
            idProprietario = imovel.proprietario_id
            imoveis = Imovel.query.filter_by(proprietario_id=idProprietario)
            return render_template("listaimoveisproprietario.html", imoveis = imoveis, idProprietario = idProprietario)
    return render_template("atualizarimoveis.html", imovel = imovel)
        
@app.route("/enderecos/<id>/atualizar", methods=['GET', 'POST'])
def atualizarEnderecos(id):
    imovel = Imovel.query.filter_by(id=id).first()        
    if request.method == "POST":
        rua = request.form.get("rua")
        numero = request.form.get("numero")
        complemento = request.form.get("complemento")
        bairro = request.form.get("bairro")
        cidade = request.form.get("cidade")
        cep = request.form.get("cep")        
        
        if  rua and numero and complemento and bairro and cidade and cep:            
            imovel.rua = rua
            imovel.numero = numero
            imovel.complemento = complemento
            imovel.bairro = bairro
            imovel.cidade = cidade
            imovel.cep = cep
            db.session.commit()
            idProprietario = imovel.proprietario_id
            imoveis = Imovel.query.filter_by(proprietario_id=idProprietario)
            return render_template("listaimoveisproprietario.html", imoveis = imoveis, idProprietario = idProprietario)
    return render_template("atualizarimoveis.html", imovel = imovel)            

@app.route("/proprietario/endereco/<id>")
def enderecoProprietario(id):
    imovel = Imovel.query.filter_by(id=id).first()
    return render_template("enderecosproprietarios.html", imovel = imovel)

@app.route("/endereco/<id>")
def enderecoImovel(id):
    endereco = Imovel.query.filter_by(id=id).first()
    return render_template("enderecosimoveis.html", endereco = endereco)

@app.route("/imoveis/lista")
def listaImoveis():
    imoveis = Imovel.query.all()
    return render_template("listaimoveis.html", imoveis = imoveis)    

@app.route("/imoveis/alugados")
def listaImoveisAlugados():
    imoveis = Imovel.query.filter_by(alugado=True)
    return render_template("listaimoveisalugados.html", imoveis = imoveis)    

@app.route("/imoveis/disponiveis")
def listaImoveisDisponiveis():
    imoveis = Imovel.query.filter_by(alugado=False)
    return render_template("listaimoveisdisponiveis.html", imoveis = imoveis)    