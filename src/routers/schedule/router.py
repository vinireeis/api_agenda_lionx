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
        return 'OLA MUNDOOO'


class ListAllContacts(Resource):
    """EXIBIR TODOS OS CONTATOS"""

    # @spec.validate(resp=Response(HTTP_200=Contato))
    def get(self):
        try:
            response = ContactsService().get_all()
            return Response(
                dumps(response), mimetype='application/json', status=200
            )
        except Exception as error:
            response = f'message: {str(error)}'
            return Response(
                dumps(response), mimetype='application/json', status=403
            )


class ListContactById(Resource):
    """EXIBIR UM CONTATO POR ID - (ID É UMA STRING)"""

    def get(self, id):
        try:
            response = ContactsService.get_by_id(id)
            return Response(
                dumps(response), mimetype='application/json', status=200
            )
        except Exception as error:
            response = f'message: {str(error)}'
            return Response(
                dumps(response), mimetype='application/json', status=403
            )


class ListContactsByLetters(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""

    def get(self, letters):
        try:
            response = ContactsService().get_by_letters(letters)
            return Response(
                dumps(response), mimetype='application/json', status=200
            )
        except Exception as error:
            response = f'message: {str(error)}'
            return Response(
                dumps(response), mimetype='application/json', status=403
            )


class RegisterContact(Resource):
    """CADASTRAR CONTATO"""

    def post(self):
        try:
            new_contact = request.get_json()
            response = ContactsService().register(new_contact)
            return Response(
                dumps(response), mimetype='application/json', status=201
            )
        except Exception as error:
            response = f'message: {str(error)}'
            return Response(
                dumps(response), mimetype='application/json', status=403
            )


class EditContact(Resource):
    """EDITAR CONTATO POR ID - (ID É UMA STRING)"""

    def put(self, id):
        contact_to_edit = request.get_json()
        edited_contact = ContactsService().update_contact(contact_to_edit, id)
        if edited_contact:
            return 'Contato editado com sucesso', 201
        else:
            return 'Não foi possível editar o contato', 500


class SoftDeleteContact(Resource):
    """EXCLUIR CONTATO POR ID - (ID É UMA STRING)"""

    def delete(self, id):
        try:
            repository.soft_delete_contact(id)
            return 'Removido com sucesso', 200
        except Exception:
            return 'Não é possível excluir, contato não foi encontrado', 404


class CountPhonesByType(Resource):
    def get():
        ...
