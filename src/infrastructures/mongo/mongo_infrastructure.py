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

        if cls.client is None:
            try:
                cls.client = MongoClient(config('MONGO_URL_CONNECTION'))
            except Exception as ex:
                log.error(
                    msg="Error on get mongo infrastructure client",
                    error=ex
                    )
                raise ex
        return cls.client
