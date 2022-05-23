# Api Agenda
from src.infrastructures.redis.infrastructure import RedisInfrastructure

# Standards
from logging import getLogger

# Third party
from decouple import config

log = getLogger()


class RedisRepository:
    redis = RedisInfrastructure.get_client()

    def set_if_not_exists(self, key, value) -> bool:
        try:
            result = self.redis.setnx(key, value)
            return result
        except Exception as ex:
            msg = 'RedisRepository::setnx::error on set data'
            log.error(msg=msg, ex=ex)
            raise ex

    def get_by_id(self, id):
        try:
            contact_encoded = self.redis.get(id)
            return contact_encoded
        except Exception as ex:
            msg = 'RedisRepository::get_by_id::error on get data'
            log.error(msg=msg, ex=ex)
            raise ex
