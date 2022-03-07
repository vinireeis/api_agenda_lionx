from src.infrastructures.mongo.mongo_infrastructure import MongoInfrastructure

from decouple import config


class MongoRepository:
    def __init__(self):
        self.mongo_client = MongoInfrastructure.get_client()
        self.database = self.mongo_client.get_database(config("DATABASE"))
        self.collection = self.database.get_collection(config("COLLECTION_NAME"))

    def get_all_contacts(self):
        all_contacts = self.collection.find({}, {"_id": 0})
        return all_contacts

    def get_contact_by_id(self, id):
        contact = self.collection.find_one(
            {"contact_id": id, "situacion": "ativo"}, {"_id": 0}
        )
        return contact

    def get_contacts_by_firsts_letters(self, letter):
        regex_filter = {"$regex": f"^{letter}", "$options": "i"}
        zero_or_more_contacts = self.collection.find(
            {"nome": regex_filter, "situacion": "ativo"}, {"_id": 0}
        )
        return zero_or_more_contacts

    def register_contact(self, novo_contato):
        self.collection.insert_one(novo_contato)

    def update_contact(self, contato_editado, id):
        self.collection.update_one({"contact_id": id}, contato_editado)

    def soft_delete_contact(self, id):
        contato = self.get_contact_by_id(id)
        contato.update(situacion="desativado")
        self.update_contact(contato, id)
