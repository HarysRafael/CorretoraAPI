from app import db

class Imovel(db.Model):
    __tablename__ = "imovel"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    area = db.Column(db.String())
    preco = db.Column(db.Float)    
    tipo = db.Column(db.String())
    alugado = db.Column(db.Boolean()) 
    proprietario_id = db.Column(db.Integer)
    rua = db.Column(db.String())    
    numero = db.Column(db.String())    
    complemento = db.Column(db.String())
    bairro = db.Column(db.String())
    cidade = db.Column(db.String())
    cep = db.Column(db.String())
            
                
    def __init__(self, area, preco, tipo, alugado, proprietario_id, rua, numero, complemento, bairro, cidade, cep):
        self.area = area
        self.preco = preco
        self.tipo = tipo
        self.alugado = alugado
        self.proprietario_id = proprietario_id
        self.rua = rua
        self.numero = numero        
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
    
db.create_all