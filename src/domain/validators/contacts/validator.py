from pydantic import BaseModel, validator, Extra
from typing import List, Optional


class Phone(BaseModel, extra=Extra.forbid):
    number: str
    type: str

    @validator('number')
    def greater_than_9_chars(cls, phone_number):
        if len(phone_number) < 10:
            raise ValueError('Número do telefone não tem todos os digitos')
        return phone_number

    @validator('type')
    def verify_type_phone(cls, phone_type):
        types = ['residential', 'commercial', 'mobile']
        if phone_type not in types:
            raise ValueError('Tipo do contato inválido')
        return phone_type


class Contact(BaseModel, extra=Extra.forbid):
    firstName: Optional[str]
    lastName: Optional[str]
    phoneList: List[Phone]
    email: str
    address: Optional[str]

    @validator('phoneList', 'email')
    def verify_values_in_keys(cls, values):
        if not values:
            raise ValueError('One or more values empty')
        return values

    @validator('email')
    def verify_email(cls, email_contato):
        if '@' not in email_contato:
            raise ValueError('Não tem @ no email')
        return email_contato


class ContactValidate:
    def __init__(self, contact_data):
        self.contact = Contact(**contact_data)


# if __name__ == '__main__':
#     dic2 = {'firstName': 102030, 'email': 'teste123', 'address': 'teste123', 'phoneList': [{'number': '123123123', 'type': 'type1'}, {'number': '123123123', 'type': 'type1'}]}

#     contato1 = Contato(**dic2)
#     print(contato1)


    # contato2 = json.loads(contato1)
    # print(type(contato2))
    # print(contato2)
