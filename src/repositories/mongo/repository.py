# Api Agenda
from src.infrastructures.mongo.mongo_infrastructure import MongoInfrastructure

# Third party
from decouple import config
from pymongo.cursor import Cursor
from pymongo.collection import InsertOneResult, UpdateResult


class MongoRepository:
    mongo_client = MongoInfrastructure.get_client()

    @classmethod
    def __get_collection(cls):
        database = cls.mongo_client.get_database(config("MONGO_DATABASE_NAME"))
        collection = database.get_collection(config("MONGO_COLLECTION_NAME"))
        return collection

    @classmethod
    def get_all_active_contacts(cls) -> Cursor:
        collection = MongoRepository.__get_collection()
        filter_active = {"active": True}
        remove_pymongo_id = {"_id": 0}
        contacts_cursor = collection.find(filter_active, remove_pymongo_id)
        return contacts_cursor

    @classmethod
    def get_all_contacts(cls) -> Cursor:
        collection = MongoRepository.__get_collection()
        filter_all = {}
        remove_pymongo_id = {"_id": 0}
        contacts_cursor = collection.find(filter_all, remove_pymongo_id)
        return contacts_cursor

    @classmethod
    def get_contact_by_id(cls, id) -> dict:
        collection = MongoRepository.__get_collection()
        filter_by_id = {"contact_id": id, "active": True}
        remove_pymongo_id = {"_id": 0}
        contact = collection.find_one(filter_by_id, remove_pymongo_id)
        return contact

    @classmethod
    def get_contacts_by_first_letters(cls, letters) -> Cursor:
        collection = MongoRepository.__get_collection()
        regex_first_letters_contact = {
            "$regex": f"^{letters}",
            "$options": "i"
        }
        filter_by_first_name_letters = {
            "firstName": regex_first_letters_contact,
            "situation": "active"
        }
        remove_pymongo_id = {"_id": 0}
        contacts_cursor = collection.find(filter_by_first_name_letters, remove_pymongo_id)
        return contacts_cursor

    @classmethod
    def register_contact(cls, new_contact) -> InsertOneResult:
        collection = MongoRepository.__get_collection()
        insert_result = collection.insert_one(new_contact)
        return insert_result

    @classmethod
    def update_contact(cls, edited_contact, id) -> UpdateResult:
        collection = MongoRepository.__get_collection()
        filter_by_id = {"contact_id": id}
        new_values = {"$set": edited_contact}
        update_result = collection.update_one(filter_by_id, new_values)
        return update_result

    @classmethod
    def soft_delete_contact(cls, id) -> UpdateResult:
        collection = MongoRepository.__get_collection()
        filter_by_id = {"contact_id": id}
        field_to_update = {"$set": {"active": False}}
        update_result = collection.update_one(filter_by_id, field_to_update)
        return update_result
