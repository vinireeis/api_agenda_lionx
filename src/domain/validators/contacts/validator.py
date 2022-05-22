# Third party
from pydantic import BaseModel, Extra, validator
from decouple import config

# Standards
from re import MULTILINE, search, sub
from typing import List, Optional
from uuid import uuid4

class Phone(BaseModel, extra=Extra.forbid):
    number: str
    type: str

    @validator("number")
    def validate_number_format(number) -> str:
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
            raise ValueError("Invalid phone number")
        return result_number

    @validator("type")
    def verify_phone_type(phone_type):
        types = ["residential", "commercial", "mobile"]
        if phone_type not in types:
            raise ValueError("Invalid phone type")
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
    def email_is_true(email) -> str:
        regex = r'^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not search(regex, email):
            raise ValueError("Invalid email")
        return email

    @validator("phoneList", "email", "firstName")
    def verify_values_in_keys(values):
        if not values:
            raise ValueError("One or more values empty")
        return values

    def to_unpacking_at_base_model(raw_contact) -> dict:
        contact = Contact(**raw_contact).dict()
        return contact
