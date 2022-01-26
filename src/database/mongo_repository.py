from xml.dom import NotFoundErr
from src.database.connection.connect_config_mongodb import BancoDeDadosMongo

banco = BancoDeDadosMongo.init_bd()


def get_all_contacts():
    return banco.consulta.find({}, {"_id": 0})


def get_contact_by_id(id):
    return banco.consulta.find_one({'contact_id': id, 'situacion':
                                    'ativo'}, {'_id': 0})


def get_contacts_by_first_letter(letter):
    regex_filter = {"$regex": f"^{letter}", "$options": "i"}
    return banco.consulta.find({'nome': regex_filter, 'situacion': 'ativo'},
                               {'_id': 0})


def register_contact(novo_contato):
    return banco.consulta.insert_one(novo_contato)


def update_contact(contato_editado, id):
    return banco.consulta.update_one({"contact_id": id},
                                     contato_editado)


def soft_delete_contact(id):
    try:
        contato = get_contact_by_id(id)
        print('-=' *30)
        print(contato)
        contato.update(situacion='desativado')
        print(contato)
        return update_contact(contato, id)
    except:
        raise NotFoundErr
