from app import db

class Telefone(db.Model):
    __tablename__ = "telefone"    
    id = db.Column(db.Integer,  primary_key = True, autoincrement = True)
    ddd = db.Column(db.String())
    numero = db.Column(db.String())
    contato = db.Column(db.String())
    id_pessoa = db.Column(db.Integer)
    
    def __init__(self, ddd, numero, contato, id_pessoa):
        self.ddd = ddd
        self.numero = numero
        self.contato = contato        
        self.id_pessoa = id_pessoa
                        
db.create_all()