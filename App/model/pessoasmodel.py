from app import db

class Pessoa(db.Model):    
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)        
    documento = db.Column(db.String())
    
    def __init__(self, documento):
        self.documento = documento    	

db.create_all()