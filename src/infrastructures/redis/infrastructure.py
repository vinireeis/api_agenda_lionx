# Standards
from logging import getLogger

# Third party
from decouple import config
from redis import from_url

log = getLogger()

class RedisInfrastructure:
    client = None

    @classmethod
    def get_client(cls):
        try:
            if cls.client is None:
                host = config('REDIS_HOST')
                client = from_url(url=host)
            return client
        except Exception as ex:
            message = f'Error on get redis client with this host::{host}'
            log.error(msg=message)
            raise ex
