from pymongo import MongoClient


class BancoDeDadosMongo:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://vihreis:abc123456@clusterreis'
                                  '.jsyr2.mongodb.net/test')
        self.database = self.client['agenda']
        self.collections = self.database['contatos']
        self.consulta = self.database.posts


banco_instancia = BancoDeDadosMongo()

'''
client = MongoClient(
    'mongodb+srv://vihreis:abc123456@clusterreis.jsyr2.mongodb.net/test')
db = client['agenda']
collections = db['contatos']
consulta = db.posts
contato = {
    "_id": 2,
    "nome": "Larissa Reis",
    "email": "lari@hotmail.com",
    "telefones": [
            {"numero": "1195295555",
                       "tipo": "celular"},
            {"numero": "26463333",
                       "tipo": "residencial"}
                      ]
        }
post = db.posts.insert_one(contato)
consulta_db = db.posts.find()
'''
