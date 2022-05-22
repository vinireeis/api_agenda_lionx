# Api Agenda
from http import HTTPStatus
from src.services.schedule.contacts import ContactsService
from src.domain.response.model import ResponseBuilder

# Third party
from flask import request
from flask_restful import Resource

class HelloWord(Resource):
    """ESSA É A ROTA DE BOAS-VINDAS"""

    def get(self):
        response = 'OLA MUNDOOO'
        return response


class ListAllContacts(Resource):
    """EXIBIR TODOS OS CONTATOS ATIVOS"""

    def get(self):
        try:
            result = ContactsService.get_all()
            response = ResponseBuilder.response_http(
                result=result,
                success=True,
                status=HTTPStatus.OK
                )
            return response
        except Exception as ex:
            error_message = f'message: {str(ex)}'
            response = ResponseBuilder.response_http(
                success=False,
                status=HTTPStatus.FORBIDDEN,
                message=error_message
                )
        return response


class ListAllContactsDb(Resource):
    """EXIBIR TODOS OS CONTATOS NO DB"""
    def get(self):
        try:
            result = ContactsService.get_all_in_db()
            response = ResponseBuilder.response_http(
                result=result,
                success=True,
                status=HTTPStatus.OK
                )
            return response
        except Exception as ex:
            error_message = f'message: {str(ex)}'
            response = ResponseBuilder.response_http(
                success=False,
                status=HTTPStatus.FORBIDDEN,
                message=error_message
                )
        return response


class ListContactById(Resource):
    """EXIBIR UM CONTATO POR ID - (ID É UMA STRING)"""

    def get(self, id):
        try:
            result = ContactsService.get_by_id(id)
            response = ResponseBuilder.response_http(
                success=True,
                result=result,
                status=HTTPStatus.OK
                )
            return response
        except Exception as error:
            error_message = f'message: {str(error)}'
            response = ResponseBuilder.response_http(
                success=False,
                message=error_message,
            )
        return response


class ListContactsByLetters(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""

    def get(self, letters):
        try:
            result = ContactsService.get_by_letters(letters)
            response = ResponseBuilder.response_http(
                success=True,
                result=result,
                status= HTTPStatus.OK
                )
            return response
        except Exception as error:
            error_message = f'message: {str(error)}'
            response = ResponseBuilder.response_http(
                success=False,
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
                message=error_message
                )
            return response


class RegisterContact(Resource):
    """CADASTRAR CONTATO"""

    def post(self):
        try:
            raw_contact = request.get_json()
            ContactsService.register(raw_contact)
            response = ResponseBuilder.response_http(
                success=True,
                message="Contact successfully created",
                status=HTTPStatus.CREATED
            )
            return response
        except Exception as error:
            error_message = f'message: {str(error)}'
            response = ResponseBuilder.response_http(
                message=error_message,
                success=False,
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
            return response


class EditContact(Resource):
    """EDITAR CONTATO POR ID - (ID É UMA STRING)"""

    def put(self, id):
        try:
            raw_contact_update = request.get_json()
            ContactsService.update(raw_contact_update, id)
            response = ResponseBuilder.response_http(
                success=True,
                message='Contact successfully updated',
                status=HTTPStatus.OK
            )
            return response
        except Exception as ex:
            error_message = f'message: {str(ex)}'
            response = ResponseBuilder.response_http(
                success=False,
                message=error_message,
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
            return response


class SoftDeleteContact(Resource):
    """EXCLUIR CONTATO POR ID - (ID É UMA STRING)"""

    def delete(self, id):
        try:
            ContactsService.soft_delete(id)
            response = ResponseBuilder.response_http(
                success=True,
                message="Contact successfully deleted",
            )
            return response
        except Exception as ex:
            message = f'message: unexpected error occurred'
            response = ResponseBuilder.response_http(
                result=False,
                message=message,
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
            return response


class CountPhonesByType(Resource):
    def get(self):
        ...
