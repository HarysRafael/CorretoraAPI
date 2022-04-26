from model.pessoasmodel import *
from controller.telefonescontroller import deletarListaTelefones

# A entidade Pessoa foi criada em conjunto às entidades
# Proprietário, Inquilino e Corretor para que houvesse
# um identificador único entre elas e com isso, fosse 
# possível relacioná-la à entidade Telefone

def cadastrarPessoa(pessoa):
    db.session.add(pessoa)        
    db.session.commit()  
    
def deletarPessoa(cpf):        
    pessoa = Pessoa.query.filter_by(documento = cpf).first()
    deletarListaTelefones(pessoa.id)
    db.session.delete(pessoa)
    db.session.commit
    