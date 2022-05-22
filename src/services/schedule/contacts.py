# Api Agenda Lionx
from src.repositories.mongo.repository import MongoRepository
from src.domain.validators.contacts import validator

# Third party
from uuid import uuid4


class ContactsService:

    @staticmethod
    def _to_list(contacts) -> list:
        return [contact for contact in contacts]

    @staticmethod
    def get_all() -> dict:
        contacts_mongo_object = MongoRepository().get_all_contacts()
        contacts_list = ContactsService._to_list(contacts_mongo_object)
        return {"contacts": contacts_list}

    @staticmethod
    def get_by_id(id) -> dict:
        contact_db = MongoRepository().get_contact_by_id(id)
        if not contact_db:
            raise Exception("Contact not found.")
        return contact_db

    @staticmethod
    def get_by_letters(letters) -> dict:
        contacts_db = MongoRepository().get_contacts_by_first_letters(letters=letters)
        contacts_list = ContactsService._to_list(contacts_db)
        if not contacts_list:
            raise Exception("Contact not found.")
        return {"contacts": contacts_list}

    @staticmethod
    def _add_contact_id(contact_validated):
        contact_validated.update(contact_id=str(uuid4()))

    @staticmethod
    def _add_activity_attr(contact_validated):
        contact_validated.update(situation="active")

    @staticmethod
    def register(raw_contact) -> dict:
        contact_validated = validator.Contact.to_unpacking_at_base_model(raw_contact=raw_contact)
        ContactsService._add_contact_id(contact_validated)
        ContactsService._add_activity_attr(contact_validated)
        MongoRepository().register_contact(contact_validated)
        return True

    @staticmethod
    def update(edited_contact, id):
        contact_exists = ContactsService.get_by_id(id=id)
        contact_validated = validator.Contact.to_unpacking_at_base_model(edited_contact)
        MongoRepository().update_contact(edited_contact=contact_validated, id=id)
        return True

    @staticmethod
    def soft_delete(id):
        contact_to_delete = ContactsService.get_by_id(id=id)
        MongoRepository().soft_delete_contact(id=id)
        contact_to_delete.update(situation="deactivated")
        response = {"message": "Contact successfully deleted"}
        return response

    @staticmethod
    def _deactivate_activity_attr(contact):
        if contact["situation"] == "active":
            contact.update(situation="deactivated")

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
