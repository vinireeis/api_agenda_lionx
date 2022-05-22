# Api Agenda
from src.infrastructures.redis.infrastructure import RedisInfrastructure

# Standards
from logging import getLogger

# Third party
from decouple import config

log = getLogger()


class RedisRepository:
    redis = RedisInfrastructure.get_client()

    def get_all(cls):
        key = config('REDIS_KEY')
        try:
            contacts_encoded = cls.redis.get(name=key)
            return contacts_encoded
        except Exception as ex:
            msg = 'error on get data'
            log.error(msg=msg, ex=ex)
            raise ex

    def get_one(cls, id):
        pass

    def set(cls, contacts) -> True:
        ex = int(config("REDIS_EXPIRATION"))
        key = config('REDIS_KEY')
        try:
            cls.redis.set(name=key, value=contacts, ex=ex)
        except Exception as ex:
            msg = 'error on set data'
            log.error(msg=msg, ex=ex)
            raise ex
