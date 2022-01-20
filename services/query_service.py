from services.manipulate_data_service import adciona_id_no_contato, adciona_situacao_no_contato
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
    adciona_situacao_no_contato(novo_contato)
    try:
        banco_instancia.consulta.insert_one(novo_contato)
    except:
        raise ErroAoCadastrar


def consultar_todos_contatos():
    todos_contatos_mongodb = banco_instancia.consulta.find({}, {"_id": 0})
    return todos_contatos_mongodb


def consultar_contato_por_id(id):
    consulta_contato = banco_instancia.consulta.find_one({"contato_id": id, 'situacao': 'ativo'}, {"_id": 0})
    # if consulta_contato:
    return consulta_contato
    # else:
    #     raise ErroContatoNaoEncontrado


def consultar_contato_por_letra(letra):
    print(letra)
    regex_busca_letras = {'$regex': f'^{letra}', '$options': 'i'}
    contatos_com_letra = banco_instancia.consulta.find({'nome': regex_busca_letras, 'situacao': 'desativado'}, {'_id': 0})
    return contatos_com_letra


def editar_um_contato(contato_editado, id):
    banco_instancia.consulta.find_one_and_update({"contato_id": id}, {'$set': contato_editado})


def remover_um_contato(id):
    banco_instancia.consulta.find_one_and_update({"contato_id": id, 'situacao': 'ativo'}, {'$set': {'situacao': 'desativado'}})
