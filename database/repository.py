from database.connection.connect_config_mongodb import BancoDeDadosMongo

banco = BancoDeDadosMongo.init_bd()


def cadastrar_um_contato(novo_contato):
    return banco.consulta.insert_one(novo_contato)


def consultar_todos_contatos():
    return banco.consulta.find({}, {"_id": 0})


def consultar_contato_por_id(id):
    return banco.consulta.find_one({"contato_id": id, 'situacao':
                                    'ativo'}, {"_id": 0})


def editar_um_contato(contato_editado, id):
    return banco.consulta.update_one({"contato_id": id},
                                     contato_editado)


def remover_um_contato(id):
    contato = banco.consulta.find_one({"contato_id": id, 'situacao': 'ativo'})
    contato.update(situacao='desativado')
    return editar_um_contato(contato, id)
