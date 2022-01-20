from uuid import uuid4


def adciona_id_no_contato(novo_contato):
    novo_contato['contato_id'] = str(uuid4())
    return novo_contato


def adciona_situacao_no_contato(novo_contato):
    novo_contato['situacao'] = 'ativo'
    return novo_contato
