# Api Agenda Lionx
from infrastructures.redis.infrastructure import RedisInfrastructure
from src.domain.exceptions.exceptions import NoRecordsFound
from src.repositories.mongo.repository import MongoRepository
from src.repositories.redis.repository import RedisRepository
from src.domain.validators.contacts import validator


class ContactsService:

    @staticmethod
    def _to_list(contacts) -> list:
        contacts_list = {
            "contacts": [contact for contact in contacts]
            }
        return contacts_list

    @staticmethod
    def get_all() -> dict:
        contacts_mongo_object = MongoRepository.get_all_active_contacts()
        contacts_list = ContactsService._to_list(contacts_mongo_object)
        return contacts_list

    @staticmethod
    def get_all_in_db() -> dict:
        contacts_mongo_object = MongoRepository.get_all_contacts()
        contacts_list = ContactsService._to_list(contacts_mongo_object)
        return contacts_list

    @staticmethod
    def get_by_id(id) -> dict:
        RedisRepository.get_by_id(id)
        contact_db = MongoRepository.get_contact_by_id(id)
        if not contact_db:
            raise NoRecordsFound
        return contact_db

    @staticmethod
    def get_by_letters(letters) -> dict:
        contacts_db = MongoRepository.get_contacts_by_first_letters(letters=letters)
        contacts_list = ContactsService._to_list(contacts_db)
        if not contacts_list:
            raise NoRecordsFound
        return contacts_list

    @staticmethod
    def register(raw_contact) -> dict:
        contact_validated = validator.Contact.to_unpacking_at_base_model(raw_contact=raw_contact)
        RedisRepository.set()
        MongoRepository.register_contact(contact_validated)
        return True

    @staticmethod
    def update(edited_contact, id):
        ContactsService.get_by_id(id=id)
        contact_validated = validator.Contact.to_unpacking_at_base_model(edited_contact)
        MongoRepository.update_contact(edited_contact=contact_validated, id=id)
        return True

    @staticmethod
    def soft_delete(id):
        ContactsService.get_by_id(id=id)
        MongoRepository.soft_delete_contact(id=id)
        response = {"message": "Contact successfully deleted"}
        return response

    @staticmethod
    def add_total_contacts_by_type(contacts_list):
        total = total_residential = total_commercial = total_mobile = 0
        for contact in contacts_list:
            for phone in contact["phoneList"]:
                total += 1
                if phone["type"] == "residential":
                    total_residential += 1
                elif phone["type"] == "commercial":
                    total_commercial += 1
                else:
                    total_mobile += 1
            response = {
                "totals": {
                    "total contacts": total,
                    "totalCommercial": total_commercial,
                    "totalMobile": total_mobile,
                    "totalResidential": total_residential,
                }
            }
            return response
