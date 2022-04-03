# Api Agenda Lionx
from src.infrastructures.mongo.mongo_infrastructure import MongoInfrastructure

# Third party
from decouple import config


class MongoRepository:
    def __init__(self):
        self.mongo_client = MongoInfrastructure.get_client()
        self.database = self.mongo_client.get_database(config("DATABASE_NAME"))
        self.collection = self.database.get_collection(config("COLLECTION_NAME"))

    def get_all_contacts(self):
        contacts_pymongo_obj = self.collection.find({}, {"_id": 0})
        return contacts_pymongo_obj

    def get_contact_by_id(self, id):
        contact = self.collection.find_one(
            {"contact_id": id, "situation": "active"}, {"_id": 0}
        )
        return contact

    def get_contacts_by_first_letters(self, letters):
        regex_filter = {"$regex": f"^{letters}", "$options": "i"}
        contacts_pymongo_obj = self.collection.find(
            {"firstName": regex_filter, "situation": "active"}, {"_id": 0}
        )
        return contacts_pymongo_obj

    def register_contact(self, new_contact):
        self.collection.insert_one(new_contact)

    def update_contact(self, edit_contact, id):
        self.collection.update_one({"contact_id": id}, edit_contact)

    def soft_delete_contact(self, id) -> dict:
        contact = self.get_contact_by_id(id)
        contact.update(situation="deactivated")
        return {"message": "Contact successfully deleted"}
