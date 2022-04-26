from app import db
                    
class Corretor(db.Model):
    __tablename__ = "corretor"    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String())      
    matricula = db.Column(db.String())
    email = db.Column(db.String())        
      
    def __init__(self, nome, matricula, email):        
        self.nome = nome
        self.matricula = matricula
        self.email = email    

db.create_all()
    