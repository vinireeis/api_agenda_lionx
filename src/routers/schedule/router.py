from flask import request
from flask_restful import Resource
from src.repositories.mongo import repository
from src.services.schedule.contacts import ContactsService


class HelloWord(Resource):
    """ESSA É A ROTA DE BOAS-VINDAS"""
    def get(self):
        return "OLA MUNDOOO"


class AgendaListarTodos(Resource):
    """EXIBIR TODOS OS CONTATOS"""
    # @spec.validate(resp=Response(HTTP_200=Contato))
    def get(self):
        return ContactsService.get_all()


class AgendaListarUmContato(Resource):
    """EXIBIR UM CONTATO POR ID - (ID É UMA STRING)"""
    def get(self, id):
        return ContactsService.get_by_id(id)


class AgendaListarPorLetra(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""
    def get(self, letters):
        return ContactsService.get_by_letters(letters)


class AgendaCadastrarContato(Resource):
    """CADASTRAR CONTATO"""
    def post(self):
        new_contact = request.get_json()
        return ContactsService.register(new_contact)


class AgendaEditarContato(Resource):
    """EDITAR CONTATO POR ID - (ID É UMA STRING)"""
    def put(self, id):
        contato_editar = request.get_json()
        contato_editado = repository.update_contact(contato_editar, id)
        if contato_editado:
            return "Contato editado com sucesso", 201
        else:
            return "Não foi possível editar o contato", 500


class AgendaExcluirContato(Resource):
    """EXCLUIR CONTATO POR ID - (ID É UMA STRING)"""
    def delete(self, id):
        try:
            repository.soft_delete_contact(id)
            return "Removido com sucesso", 200
        except:
            return 'Não é possível excluir, contato não foi encontrado', 404


class AgendaCountPhonesByType(Resource):
    def get():
        pass
