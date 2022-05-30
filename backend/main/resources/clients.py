from flask_restful import Resource
from flask import jsonify, request

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
        client = request.get_json()
        clients.append(client)
        return client, 201
    
class Client(Resource):
    
    def get(self, id):
        return jsonify({
            'client': clients[int(id)]
        })
        
    def delete(self, id):
        return 
    