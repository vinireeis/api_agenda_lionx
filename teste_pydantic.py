from pydantic import BaseModel, validator
import json


class Telefone(BaseModel):
    numero: str
    type: str

    @validator('numero')
    def telefone_maior_9_chars(cls, numero_contato):
        if len(numero_contato) < 10:
            raise ValueError('Número do telefone não tem todos os digitos')
        return numero_contato

    @validator('type')
    def tem_tipo_correto(cls, tipo_contato):
        tipos = ['residencial', 'comercial', 'celular']
        if tipo_contato not in tipos:
            raise ValueError('Tipo do contato inválido')
        return tipo_contato


class Contato(BaseModel):
    nome: str
    telefones: list[Telefone]
    email: str
    endereco: str

    @validator('*')
    def tem_valor_nas_chaves(cls, dados_contato):
        if not dados_contato:
            raise ValueError('Existe um ou mais campos não preenchidos')
        return dados_contato

    @validator('email')
    def tem_arroba_no_email(cls, email_contato):
        if '@' not in email_contato:
            raise ValueError('Não tem @ no email')
        return email_contato


# if __name__ == '__main__':
#     dic2 = {'nome': 102030, 'email': 'teste123', 'endereco': 'teste123', 'telefone': [{'numero': '123123123', 'tipo': 'type1'}, {'numero': '123123123', 'tipo': 'type1'}]}

#     contato1 = Contato(**dic2).json()
#     print(contato1)

    # contato2 = json.loads(contato1)
    # print(type(contato2))
    # print(contato2)
