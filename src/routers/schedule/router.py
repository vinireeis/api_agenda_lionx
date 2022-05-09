# Api Agenda Lionx
from src.repositories.mongo import repository
from src.services.schedule.contacts import ContactsService

# Third party
from flask import request, Response
from flask_restful import Resource

# Standards
from json import dumps


class HelloWord(Resource):
    """ESSA É A ROTA DE BOAS-VINDAS"""

    def get(self):
        response = 'OLA MUNDOOO'
        return response


class ListAllContacts(Resource):
    """EXIBIR TODOS OS CONTATOS"""

    def get(self):
        try:
            response_service = ContactsService().get_all()
            response = Response(
                dumps(response_service), mimetype='application/json', status=200
            )
            return response
        except Exception as ex:
            error_message = f'message: {str(ex)}'
            response = Response(
                dumps(error_message), mimetype='application/json', status=403
            )
        return response


class ListContactById(Resource):
    """EXIBIR UM CONTATO POR ID - (ID É UMA STRING)"""

    def get(self, id):
        try:
            response_service = ContactsService.get_by_id(id)
            response = Response(
                dumps(response_service), mimetype='application/json', status=200
            )
            return response
        except Exception as error:
            error_message = f'message: {str(error)}'
            response = Response(
                dumps(error_message), mimetype='application/json', status=403
            )
        return response


class ListContactsByLetters(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""

    def get(self, letters):
        try:
            response_service = ContactsService().get_by_letters(letters)
            response = Response(
                dumps(response_service), mimetype='application/json', status=200
            )
            return response
        except Exception as error:
            error_message = f'message: {str(error)}'
            response = Response(
                dumps(error_message), mimetype='application/json', status=403
            )
            return response


class RegisterContact(Resource):
    """CADASTRAR CONTATO"""

    def post(self):
        try:
            new_contact = request.get_json()
            response_service = ContactsService().register(new_contact)
            response = Response(
                dumps(response_service), mimetype='application/json', status=200
            )
            return response
        except Exception as error:
            error_message = f'message: {str(error)}'
            response =Response(
                dumps(error_message), mimetype='application/json', status=403
            )
            return response


class EditContact(Resource):
    """EDITAR CONTATO POR ID - (ID É UMA STRING)"""

    def put(self, id):
        try:
            contact_to_edit = request.get_json()
            response_service = ContactsService().update(contact_to_edit, id)
            response = Response(
                    dumps(response_service), mimetype='application/json', status=200
                )
            return response
        except Exception as error:
            error_message = f'message: {str(error)}'
            response = Response(
                dumps(error_message), mimetype='application/json', status=403
            )
            return response


class SoftDeleteContact(Resource):
    """EXCLUIR CONTATO POR ID - (ID É UMA STRING)"""

    def delete(self, id):
        try:
            response_service = ContactsService().soft_delete(id)
            response = Response(
                    dumps(response_service), mimetype='application/json', status=200
                )
            return response
        except Exception as error:
            message = f'message: {str(error)}'
            response = Response(
                dumps(message), mimetype='application/json', status=403
            )
            return response


class CountPhonesByType(Resource):
    def get(self):
        ...
