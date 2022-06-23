# Standards
from re import MULTILINE, search, sub
from typing import List, Optional
from uuid import uuid4

# Third party
from decouple import config
from loguru import logger
from pydantic import BaseModel, Extra, validator


class Phone(BaseModel, extra=Extra.forbid):
    number: str
    type: str

    @validator("number")
    def validate_number_format(cls, number) -> str:
        regex = r"[\D]"
        subst = ""
        result_number = sub(
            regex,
            subst,
            number,
            int(config("VALIDATE_NUMBER")),
            MULTILINE
            )
        if not result_number:
            msg = "Invalid phone number"
            logger.info(msg)
            raise ValueError(msg)
        return result_number

    @validator("type")
    def verify_phone_type(cls, phone_type):
        types = ["residential", "commercial", "mobile"]
        if phone_type not in types:
            msg = "Invalid phone type"
            logger.info(msg)
            raise ValueError(msg)
        return phone_type


class Contact(BaseModel, extra=Extra.forbid):
    firstName: str
    lastName: Optional[str]
    phoneList: List[Phone]
    email: str
    address: Optional[str]
    contact_id: str = (uuid4())
    active: bool = True

    @validator("email")
    def email_is_true(cls, email) -> str:
        regex = r'^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not search(regex, email):
            msg = "Invalid email"
            logger.info(msg)
            raise ValueError(msg)
        return email

    @validator("phoneList", "email", "firstName")
    def verify_values_in_keys(cls, values):
        if not values:
            msg = "One or more values empty"
            logger.info(msg)
            raise ValueError(msg)
        return values

    @staticmethod
    def to_unpacking_at_base_model(raw_contact) -> dict:
        contact = Contact(**raw_contact).dict()
        return contact
