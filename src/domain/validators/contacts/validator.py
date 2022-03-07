from pydantic import BaseModel, Extra, validator
from re import MULTILINE, search, sub
from typing import List, Optional


class Phone(BaseModel, extra=Extra.forbid):
    number: str
    type: str

    @validator("number")
    def validate_and_format_numer(number):
        regex = r"[\D]"
        subst = ""
        result_number = sub(regex, subst, number, 0, MULTILINE)
        if not result_number:
            raise ValueError("Invalid phone number")
        return result_number

    @validator("type")
    def verify_type_phone(cls, phone_type):
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

    @validator("email")
    def email_is_true(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not search(regex, email):
            raise ValueError("Invalid email")
        return email

    @validator("phoneList", "email", "firstName")
    def verify_values_in_keys(cls, values):
        if not values:
            raise ValueError("One or more values empty")
        return values

    def validate_unpacking(contact_data):
        contact = Contact(**contact_data).dict()
        return contact


# if __name__ == "__main__":
#     dic2 = {
#         "firstName": "Vinicius Reis",
#         "email": "teste@123.com",
#         "address": "Rua logo ali 123",
#         "phoneList": [
#             {"number": "11952945737", "type": "commercial"},
#             {"number": "1126467579", "type": "commercial"},
#         ],
#     }

#     contato1 = Contact.validate_unpacking(dic2)
#     print(contato1)
