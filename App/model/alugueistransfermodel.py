from app import db

class AluguelTransfer(db.Model):
    __tablename__ = "alugueltransfer"    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)    
    inquilino_id = db.Column(db.Integer)    
    corretor_id = db.Column(db.Integer)
    imovel_id = db.Column(db.Integer)
    idRandom = db.Column(db.String())

    def __init__(self, inquilino_id, corretor_id, imovel_id, idRandom):        
        self.inquilino_id = inquilino_id
        self.corretor_id = corretor_id
        self.imovel_id = imovel_id                
        self.idRandom = idRandom    

db.create_all()

