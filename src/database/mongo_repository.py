from database.connection.connect_config_mongodb import BancoDeDadosMongo

banco = BancoDeDadosMongo.init_bd()


def get_all_contacts():
    return banco.consulta.find({}, {"_id": 0})


def get_contact_by_id(id):
    return banco.consulta.find_one({'contato_id': id, 'situacao':
                                    'ativo'}, {'_id': 0})


def get_contacts_by_first_letter(letter):
    return banco.consulta.find({'name': '$regex', '$options': '-i'}, {'_id': 0})


def register_contact(novo_contato):
    return banco.consulta.insert_one(novo_contato)


def update_contact(contato_editado, id):
    return banco.consulta.update_one({"contato_id": id},
                                     contato_editado)


def soft_delete_contact(id):
    contato = banco.consulta.find_one({"contato_id": id, 'situacao': 'ativo'})
    contato.update(situacao='desativado')
    return update_contact(contato, id)
