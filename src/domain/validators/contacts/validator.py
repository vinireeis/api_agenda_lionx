from typing import Optional
from pydantic import BaseModel, validator, Extra


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
    phoneList: list[Phone]
    email: str
    address: Optional[str]

    @validator('phoneList', 'email')
    def verify_values_in_keys(cls, values):
        if not values:
            raise ValueError('Existe um ou mais campos não preenchidos')
        return values

    @validator('email')
    def verify_email(cls, email_contato):
        if '@' not in email_contato:
            raise ValueError('Não tem @ no email')
        return email_contato


# if __name__ == '__main__':
#     dic2 = {'nome': 102030, 'email': 'teste123', 'address': 'teste123', 'telefone': [{'numero': '123123123', 'tipo': 'type1'}, {'numero': '123123123', 'tipo': 'type1'}]}

#     contato1 = Contato(**dic2).json()
#     print(contato1)

    # contato2 = json.loads(contato1)
    # print(type(contato2))
    # print(contato2)
