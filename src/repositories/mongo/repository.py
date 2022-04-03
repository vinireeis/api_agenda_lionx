# Api Agenda Lionx
from src.infrastructures.mongo.mongo_infrastructure import MongoInfrastructure

# Third party
from decouple import config
from pymongo.cursor import Cursor
from pymongo.collection import InsertOneResult, UpdateResult

class MongoRepository:
    def __init__(self):
        self.mongo_client = MongoInfrastructure.get_client()
        self.database = self.mongo_client.get_database(config("DATABASE_NAME"))
        self.collection = self.database.get_collection(config("COLLECTION_NAME"))

    def get_all_contacts(self) -> Cursor:
        remove_pymongo_id = {"_id": 0}
        contacts_cursor = self.collection.find({}, remove_pymongo_id)
        return contacts_cursor

    def get_contact_by_id(self, id) -> dict:
        filter_by_id = {"contact_id": id, "situation": "active"}
        remove_pymongo_id = {"_id": 0}
        contact = self.collection.find_one(filter_by_id, remove_pymongo_id)
        return contact

    def get_contacts_by_first_letters(self, letters) -> Cursor:
        regex_first_letters_contact = {"$regex": f"^{letters}", "$options": "i"}
        filter_by_first_name_letters = {"firstName": regex_first_letters_contact, "situation": "active"}
        remove_pymongo_id = {"_id": 0}
        contacts_cursor = self.collection.find(filter_by_first_name_letters, remove_pymongo_id)
        return contacts_cursor

    def register_contact(self, new_contact) -> InsertOneResult:
        insert_result = self.collection.insert_one(new_contact)
        return insert_result

    def update_contact(self, edited_contact, id) -> UpdateResult:
        filter_by_id = {"contact_id": id}
        new_values = {"$set": edited_contact}
        update_result = self.collection.update_one(filter_by_id, new_values)
        return update_result

    def soft_delete_contact(self, id) -> UpdateResult:
        filter_by_id = {"contact_id": id}
        field_to_update = {"$set": {"situation": "deactivated"}}
        update_result = self.collection.update_one(filter_by_id, field_to_update)
        return update_result
