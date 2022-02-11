from enum import Enum, IntEnum


class RegionEnum(str, Enum):
    br = 'br'
    us = 'us'


class StatusCodeEnum(IntEnum):
    sucess = 200
    bad_request = 403
    internal_server_error = 500