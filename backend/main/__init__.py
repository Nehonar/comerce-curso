import os
from flask import Flask
from dotenv import load_dotenv

# API rest module
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    
    load_dotenv()
    
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        db_file = os.open(f'{PATH}/{DB_NAME}', os.O_CREAT)
        os.close(db_file)
    
    app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
    db.init_app(app)
    
    import main.resources as resources
    api.add_resource(resources.AllClientsResource, '/clients')
    api.add_resource(resources.ClientResource, '/clients/<id>')
    
    api.init_app(app)
    
    return app