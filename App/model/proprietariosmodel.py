from app import db
                    
class Proprietario(db.Model):
    __tablename__ = "proprietario"    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String())      
    cpf = db.Column(db.String())   
    email = db.Column(db.String())        
      

    def __init__(self, nome, cpf, email):        
        self.nome = nome
        self.cpf = cpf
        self.email = email    

db.create_all()
    