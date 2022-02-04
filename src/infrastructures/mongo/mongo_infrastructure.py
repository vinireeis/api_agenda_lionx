from pymongo import MongoClient
from decouple import config


class MongoInfrastrucutre:
    client = None

    @staticmethod
    def get_client():
        if MongoInfrastrucutre.client is None:
            MongoInfrastrucutre.client = MongoClient(config('MONGO_CONNECTION'))
        return MongoInfrastrucutre.client


'''
class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://vihreis:abc123456@clusterreis'
                                  '.jsyr2.mongodb.net/test')
        self.database = self.client['agenda']
        self.collections = self.database['contatos']
        self.consulta = self.database.posts
'''
