from uuid import uuid4
from db.conexao_mongodb import banco_instancia


class ErroAoCadastrar(Exception):
    pass


class ErroAoEditar(Exception):
    pass


class ErroAoExcluir(Exception):
    pass


class ErroContatoNaoEncontrado(Exception):
    pass


def cadastrar_um_contato(novo_contato):
    adciona_id_no_contato(novo_contato)
    try:
        banco_instancia.consulta.insert_one(novo_contato)
    except:
        raise ErroAoCadastrar


def adciona_id_no_contato(novo_contato):
    novo_contato['contato_id'] = str(uuid4())
    return novo_contato


def adciona_situacao_no_contato(novo_contato):
    novo_contato['situacao'] = 'ativo'
    return novo_contato


def consultar_todos_contatos():
    todos_contatos_mongodb = banco_instancia.consulta.find({}, {"_id": 0})
    return todos_contatos_mongodb


def consultar_contato_por_id(id):
    consulta_contato = banco_instancia.consulta.find_one({"contato_id": id}, {"_id": 0})
    if consulta_contato:
        return consulta_contato
    else:
        raise ErroContatoNaoEncontrado


def editar_um_contato(contato_editado, id):
    try:
        banco_instancia.consulta.find_one_and_replace({"contato_id": id},
                                                      contato_editado)
    except:
        raise ErroAoEditar


def remover_um_contato(id):
    try:
        banco_instancia.consulta.find_one_and_delete({"_id": id})
    except:
        raise ErroAoExcluir
