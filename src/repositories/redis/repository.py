# Api Agenda
from src.infrastructures.redis.infrastructure import RedisInfrastructure

# Third party
from loguru import logger


class RedisRepository:
    redis = RedisInfrastructure.get_client()

    def set_if_not_exists(self, key, value) -> bool:
        try:
            result = self.redis.setnx(key, value)
            return result
        except Exception as ex:
            msg = f'RedisRepository::setnx::error on set data::{ex}'
            logger.error(msg)
            raise ex

    def get_by_id(self, id):
        try:
            contact_encoded = self.redis.get(id)
            return contact_encoded
        except Exception as ex:
            msg = f'RedisRepository::get_by_id::error on get data::{ex}'
            logger.error(msg)
            raise ex
