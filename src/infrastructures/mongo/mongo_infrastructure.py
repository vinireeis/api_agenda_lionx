# Third party
from decouple import config
from pymongo import MongoClient

# Standards
from logging import getLogger

log = getLogger()


class MongoInfrastructure:
    client = None

    @classmethod
    def get_client(cls):

        if MongoInfrastructure.client is None:
            try:
                MongoInfrastructure.client = MongoClient(config('MONGO_CONNECTION'))
                return MongoInfrastructure.client
            except Exception as ex:
                log.error(msg="Error on get mongo infrastructure client", error=ex)
                raise ex
