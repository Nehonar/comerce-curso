from flask_restful import Resource
from flask import jsonify

clients = [
    {
        "id": 1,
        "name": "Benito",
        "second_name": "Avila"
    },
    {
        "id": 2,
        "name": "Mireia",
        "second_name": "Plata"
    }
]

class AllClients(Resource):
    
    def get(self):
        return jsonify({
            'clients': clients
        })
    
    def post(self):
        return
    
class Client(Resource):
    
    def get(self, id):
        return jsonify({
            'client': clients[int(id)]
        })
    