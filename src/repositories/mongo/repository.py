from infrastructures.mongo.mongo_infrastructure import MongoInfrastrucutre


class MongoRepository:
    def __init__(self, database_url, collection_name):
        self.mongo_client = MongoInfrastrucutre.get_client()
        self.database = self.mongo_client.get_database(database_url)
        self.collection = self.database.get_collection(collection_name)

    def get_all_contacts(self):
        return self.collection.find({}, {"_id": 0})

    def get_contact_by_id(self, id):
        return self.collection.find_one({'contact_id': id, 'situacion':
                                         'ativo'}, {'_id': 0})

    def get_contacts_by_first_letter(self, letter):
        regex_filter = {"$regex": f"^{letter}", "$options": "i"}
        return self.collection.find({'nome': regex_filter,
                                     'situacion': 'ativo'}, {'_id': 0})

    def register_contact(self, novo_contato):
        return self.collection.insert_one(novo_contato)

    def update_contact(self, contato_editado, id):
        return self.collection.update_one({"contact_id": id}, contato_editado)

    def soft_delete_contact(self, id):
        contato = self.get_contact_by_id(id)
        contato.update(situacion='desativado')
        return self.update_contact(contato, id)
