# Third party
from decouple import config
from loguru import logger
from pymongo import MongoClient


class MongoInfrastructure:
    client = None

    @classmethod
    def get_client(cls):
        if cls.client is None:
            try:
                cls.client = MongoClient(config('MONGO_URL_CONNECTION'))
            except Exception as ex:
                msg = f"Error on get mongo infrastructure client::{ex}"
                logger.error(msg)
                raise ex
        return cls.client
