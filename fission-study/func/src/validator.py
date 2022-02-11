from pydantic import BaseModel, Extra, validator
from src.enum import RegionEnum


class ParamsJson(BaseModel, extra=Extra.forbid):
    symbol: str
    region: RegionEnum

    @validator('symbol')
    def is_empty(symbol):
        if not symbol:
            raise ValueError("Symbol is empty.")
        return symbol

    @validator('symbol')
    def is_alpha(symbol):
        if symbol.isnumeric():
            raise ValueError('Wrong format type')
        return symbol

    @validator('region')
    def is_numeric(region):
        if not region.isalpha():
            raise ValueError('Wrong format type')
        return region

    @staticmethod
    def pydantic_validate(json: dict):
        return ParamsJson(**json)
