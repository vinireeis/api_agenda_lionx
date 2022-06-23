# Third party
from decouple import config
from loguru import logger
from redis import from_url


class RedisInfrastructure:
    client = None
    url = config('REDIS_HOST')

    @classmethod
    def get_client(cls):
        try:
            if cls.client is None:
                cls.client = from_url(url=cls.url)
            return cls.client
        except Exception as ex:
            msg = f'Error on get redis client with this host::{config("REDIS_HOST")}::{ex}'
            logger.error(msg)
            raise ex
