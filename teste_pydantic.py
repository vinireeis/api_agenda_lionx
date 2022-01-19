from pydantic import BaseModel, validator
import json


class Telefone(BaseModel):
    numero: str
    tipo: str


class Contato(BaseModel):
    nome: str
    telefones: list[Telefone]
    email: str
    endereco: str

    @validator('*')
    def valida_se_tem_valor_nas_chaves(cls, dados_contato):
        if not dados_contato:
            raise ValueError('Existe um ou mais campos não preenchidos')
        return dados_contato

    @validator('email')
    def valida_se_tem_arroba(cls, email_contato):
        if '@' not in email_contato:
            raise ValueError('Não tem @ no email')
        return email_contato

    @validator('telefones')
    def valida_telefone_maior_9_chars(cls, telefones_contato):
        for telefone in telefones_contato:
            print(telefone['numero'])

# if __name__ == '__main__':
#     dic2 = {'nome': 102030, 'email': 'teste123', 'endereco': 'teste123', 'telefone': [{'numero': '123123123', 'tipo': 'type1'}, {'numero': '123123123', 'tipo': 'type1'}]}

#     contato1 = Contato(**dic2).json()
#     print(contato1)

    contato2 = json.loads(contato1)
    print(type(contato2))
    print(contato2)
