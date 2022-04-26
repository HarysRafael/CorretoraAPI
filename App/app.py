from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/corretoraapi"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controller.index import *
from controller.alugueiscontroller import *
from controller.pessoascontroller import *
from controller.proprietarioscontroller import *
from controller.inquilinoscontroller import *
from controller.corretorescontroller import *
from controller.imoveiscontroller import *

if __name__ == '__main__':   
   db.create_all()
   app.run(debug = True)