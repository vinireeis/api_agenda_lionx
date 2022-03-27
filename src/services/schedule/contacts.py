from src.repositories.mongo.repository import MongoRepository
from src.domain.validators.contacts import validator

from uuid import uuid4


class ContactsService:

    @staticmethod
    def _to_list(object_contacts):
        return [contact for contact in object_contacts]

    def get_all(self):
        contacts_db = MongoRepository().get_all_contacts()
        contacts_list = self._to_list(contacts_db)
        if not contacts_list:
            return {[], 200}
        return contacts_list

    @staticmethod
    def get_by_id(id):
        contact_db = MongoRepository().get_contact_by_id(id)
        if not contact_db:
            raise Exception("Contact not found.")
        return contact_db

    def get_by_letters(self, letters):
        contacts_db = MongoRepository().get_contacts_by_first_letters(letters)
        contacts_list = self._to_list(contacts_db)
        if not contacts_list:
            raise Exception("Contact not found.")
        return contacts_list

    def register(self, new_contact):
        contact_validated = validator.Contact.validate_basemodel(new_contact)
        self._add_contact_id(contact_validated)
        self._add_activity_attr(contact_validated)
        MongoRepository().register_contact(contact_validated)
        return {'response': 'contact created'}

    @staticmethod
    def _add_contact_id(contact_validated):
        contact_validated.update(contact_id=str(uuid4()))

    @staticmethod
    def _add_activity_attr(contact_validated):
        contact_validated.update(situation="active")

    @staticmethod
    def _deactivate_activity_attr(contato):
        if contato["situacion"] == "active":
            contato.update(situacao="deactivated")

    @staticmethod
    def add_total_contacts_by_type(lista_contatos):
        total = total_residential = total_commercial = total_mobile = 0
        for contato in lista_contatos:
            # for phone in contato['phoneList']:
            for phone in contato["telefones"]:
                total += 1
                if phone["type"] == "residential":
                    total_residential += 1
                elif phone["type"] == "commercial":
                    total_commercial += 1
                else:
                    total_mobile += 1
            dic_retorno = {
                "totals": {
                    "total": total,
                    "totalCommercial": total_commercial,
                    "totalMobile": total_mobile,
                    "totalResidential": total_residential,
                },
                "contacts": lista_contatos,
            }
        return dic_retorno


def add_totals_in_contact_dict(contatos, dic_totais):
    contatos.update(dic_totais)
    return contatos


if __name__ == "__main__":
    lista_de_contatos = [
        {
            "nome": "Vinicius Reis",
            "email": "vinicius@hotmail.com",
            "telefones": [
                {"numero": "11952945737", "type": "mobile"},
                {"numero": "26467579", "type": "residencial"},
            ],
        },
        {
            "nome": "Larissa Reis",
            "email": "lari@hotmail.com",
            "telefones": [
                {"numero": "1195295555", "type": "mobile"},
                {"numero": "26463333", "type": "residencial"},
            ],
        },
        {
            "nome": "teste create vini",
            "email": "teste@hotmail.com",
            "telefones": [
                {"numero": "1195295555", "type": "commercial"},
                {"numero": "26463333", "type": "residential"},
            ],
        },
        {
            "nome": "Mãe",
            "email": "cintia_dro@hotmail.com",
            "telefones": [
                {"numero": "1195295555", "type": "commercial"},
                {"numero": "26463333", "type": "residential"},
            ],
        },
        {
            "nome": "Vinicius Reis",
            "email": "vinicius@hotmail.com",
            "telefones": [
                {"numero": "11952945737", "type": "mobile"},
                {"numero": "26467579", "type": "residential"},
            ],
            "endereco": "Rua etcetal, 45",
        },
        {
            "nome": "Vinicius Reis",
            "email": "vinicius@hotmail.com",
            "telefones": [
                {"numero": "11952945737", "type": "mobile"},
                {"numero": "26467579", "type": "residential"},
            ],
            "endereco": "Rua etcetal, 45",
            "contato_id": "9d9d50b1-fd25-45b5-bbff-acd5baa6640e",
            "situacao": "desativado",
        },
        {
            "nome": "ViniciusUPDATE",
            "email": "teste@teste",
            "telefones": [
                {"numero": "1123123123", "type": "residencial"},
                {"numero": "1226467323", "type": "commercial"},
            ],
            "endereco": "teste123",
            "contato_id": "44ba4f8f-393c-490a-9aec-5a49d82d3639",
            "situacao": "desativado",
        },
        {
            "nome": 102030,
            "email": "teste@teste",
            "endereco": "teste123",
            "telefones": [
                {"numero": "1123123123", "type": "residencial"},
                {"numero": "1226467323", "type": "commercial"},
            ],
            "contato_id": "fbb50289-6d7d-47f8-b410-905e9da20f48",
            "situacao": "ativo",
        },
    ]
    dic = add_totals_in_contact_dict(lista_de_contatos)

    print(dic["totals"])
