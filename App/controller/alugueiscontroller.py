from app import app
from flask import render_template, request, flash, url_for
from model.alugueismodel import *
from model.corretoresmodel import Corretor
from model.inquilinosmodel import Inquilino
from model.imoveismodel import Imovel
from model.alugueistransfermodel import AluguelTransfer
import random

# Arquivo com rotas relacionadas a aluguéis desde sua criação 
# atrelada e possibilitada apenas pelo campo de Corretores 
# (como uma espécie de restrição), escolha de inquilino, imóvel, bem como 
# sua visualização, após o registro criado.
# Há a possibilidade de ver a Lista de todos Aluguéis, Aluguéis por Corretor
# e os detalhes do aluguel como: Imóvel, Endereço e Inquilino.
# Primeiramente é criado uma entidade AluguelTransfer, para que, com os dados 
# dela seja montada a entidade Aluguel.
# Após a criação de Aluguel, AluguelTransfer é excluída.

@app.route("/alugueis")
def alugueis():
    return render_template("alugueis.html")

@app.route("/corretor/<int:corretorId>/alugueis")
def alugueisCorretores(corretorId):    
    return render_template("alugueiscorretores.html", corretorId = corretorId)

@app.route("/corretor/<int:corretorId>/novoaluguel")
def novoAluguel(corretorId):        
    idRandom  = random.random()
    aluguelTransfer = AluguelTransfer(0,corretorId,0,str(idRandom))
    db.session.add(aluguelTransfer)
    db.session.commit()    
    inquilinos = Inquilino.query.all()
    return render_template("listaaluguelinquilinos.html", idRandom = idRandom, inquilinos = inquilinos)

@app.route("/corretor/<int:corretorId>/listaalugueis")
def listaAlugueisCorretores(corretorId):    
    alugueis = Aluguel.query.filter_by(corretor_id=corretorId)
    return render_template("listaalugueiscorretores.html", corretorId = corretorId, alugueis = alugueis)

@app.route("/corretor/<idRandom>/listainquilinos")
def listaAluguelInquilinos(idRandom):    
    inquilinos = Inquilino.query.all()        
    return render_template("listaaluguelinquilinos", inquilinos = inquilinos, idRandom = idRandom)

@app.route("/aluguel/<idRandom>/selecionarinquilino/<int:inquilinoId>")
def selecionarInquilino(idRandom, inquilinoId):    
    aluguelTransfer = AluguelTransfer.query.filter_by(idRandom = idRandom).first()
    aluguelTransfer.inquilino_id = inquilinoId
    db.session.commit()
    imoveis = Imovel.query.filter_by(alugado=False)
    return render_template("listaaluguelimoveis.html", idRandom = idRandom, imoveis = imoveis)            

@app.route("/aluguel/<idRandom>/listaimoveis")
def listaAluguelImoveis(idRandom):
    imoveis = Imovel.query.filter_by(alugado=False)
    return render_template("listaaluguelimoveis.html", imoveis = imoveis, idRandom = idRandom)

@app.route("/aluguel/<idRandom>/endereco/<id>")
def aluguelEndereco(idRandom, id):
    endereco = Imovel.query.filter_by(id=id).first()    
    return render_template("aluguelendereco.html", endereco = endereco, idRandom = idRandom)

@app.route("/aluguel/<idRandom>/selecionarimovel/<int:imovelId>")
def selecionarImovel(idRandom, imovelId):
    aluguelTransfer = AluguelTransfer.query.filter_by(idRandom = idRandom).first()    
    imovel = Imovel.query.filter_by(id = imovelId).first()
    imovel.alugado = True
    aluguelTransfer.imovel_id = imovel.id    
    db.session.commit()
    return render_template("cadastroaluguel.html", idRandom = idRandom)

@app.route("/aluguel/<idRandom>/cadastro")
def cadastroAluguel(idRandom):    
    return render_template("cadastroaluguel.html", idRandom = idRandom)

@app.route("/aluguel/<idRandom>/cadastrar", methods=['GET', 'POST'])
def cadastrarAluguel(idRandom):    
    aluguelTransfer = AluguelTransfer.query.filter_by(idRandom=idRandom).first()
    if request.method == "POST":   
        if not request.form['duracao_meses']:
            flash('Preencha o período de aluguel do imóvel!', 'Erro!')
        else:            
            duracao_meses = request.form['duracao_meses']
            aluguel = Aluguel(duracao_meses, aluguelTransfer.inquilino_id, aluguelTransfer.corretor_id, aluguelTransfer.imovel_id)
            db.session.delete(aluguelTransfer)
            db.session.add(aluguel)                    
            db.session.commit()            
    return render_template("index.html", )                

@app.route("/aluguel/listar")
def listaAlugueis():
    alugueis = Aluguel.query.all()
    return render_template("listaalugueis.html", alugueis = alugueis)

@app.route("/aluguel/<int:aluguelId>")
def detalhesAluguel(aluguelId):    
    aluguel = Aluguel.query.filter_by(id = aluguelId).first()    
    inquilino = Inquilino.query.filter_by(id = aluguel.inquilino_id).first()
    corretor = Corretor.query.filter_by(id = aluguel.corretor_id).first()
    imovel = Imovel.query.filter_by(id = aluguel.imovel_id).first()
    return render_template("detalhesaluguel.html", aluguel = aluguel, inquilino = inquilino, corretor =  corretor, imovel = imovel)


