from app import db

class Aluguel(db.Model):
    __tablename__ = "aluguel"    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    duracao_meses = db.Column(db.Integer)    
    inquilino_id = db.Column(db.Integer)    
    corretor_id = db.Column(db.Integer)
    imovel_id = db.Column(db.Integer) 
    
    def __init__(self, duracao_meses, inquilino_id, corretor_id, imovel_id):
        self.duracao_meses = duracao_meses        
        self.inquilino_id = inquilino_id
        self.corretor_id = corretor_id
        self.imovel_id = imovel_id                

db.create_all()