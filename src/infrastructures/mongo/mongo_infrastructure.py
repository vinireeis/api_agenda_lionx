from decouple import config
from pymongo import MongoClient


class MongoInfrastructure:
    client = None

    @classmethod
    def get_client(self):
        if MongoInfrastructure.client is None:
            MongoInfrastructure.client = MongoClient(config('MONGO_CONNECTION'))
        return MongoInfrastructure.client
