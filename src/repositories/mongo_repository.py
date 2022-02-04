from infrastructures.connection_mongo.connector_mongodb import MongoDB

instance_db = MongoDB()


def get_all_contacts():
    return instance_db.consulta.find({}, {"_id": 0})


def get_contact_by_id(id):
    return instance_db.consulta.find_one({'contact_id': id, 'situacion':
                                    'ativo'}, {'_id': 0})


def get_contacts_by_first_letter(letter):
    regex_filter = {"$regex": f"^{letter}", "$options": "i"}
    return instance_db.consulta.find({'nome': regex_filter, 'situacion': 'ativo'},
                               {'_id': 0})


def register_contact(novo_contato):
    return instance_db.consulta.insert_one(novo_contato)


def update_contact(contato_editado, id):
    return instance_db.consulta.update_one({"contact_id": id},
                                     contato_editado)


def soft_delete_contact(id):
    try:
        contato = get_contact_by_id(id)
        contato.update(situacion='desativado')
        return update_contact(contato, id)
    except:
        raise ValueError
