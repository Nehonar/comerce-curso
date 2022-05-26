import os
from flask import Flask
from dotenv import load_dotenv

# API rest module
from flask_restful import Api

api = Api()

def create_app():
    
    app = Flask(__name__)
    load_dotenv()
    
    import main.resources as resources
    api.add_resource(resources.AllClientsResource, '/all_clients')
    api.add_resource(resources.ClientResource, '/client/<id>')
    
    api.init_app(app)
    
    return app