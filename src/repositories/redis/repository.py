# Api Agenda
from src.infrastructures.redis.infrastructure import RedisInfrastructure

# Standards
from logging import getLogger

# Third party
from decouple import config

log = getLogger()

def get_all():
    redis = RedisInfrastructure.get_client()
    contacts_encoded = redis.get(name=config('REDIS_KEY'))
    return contacts_encoded

def get_one(id):
    pass

def set(contacts) -> True:
    redis = RedisInfrastructure.get_client()
    try:
        redis.set(name=config('REDIS_KEY'), value=contacts, ex=3600)
        return True
    except Exception as ex:
        message = 'error on set data'
        log.error(msg=message, ex=ex)
        raise ex
