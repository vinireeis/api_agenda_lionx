from ast import Raise
from xml.dom import NotFoundErr
from flask import request
from flask_restful import Resource
from src.database import mongo_repository
from src.resources import helpers
from json import dumps

class HelloWord(Resource):
    """ESSA É A ROTA DE BOAS-VINDAS"""
    def get(self):
        return "OLA MUNDOOO"


class AgendaListarTodos(Resource):
    """EXIBIR TODOS OS CONTATOS"""
    # @spec.validate(resp=Response(HTTP_200=Contato))
    def get(self):
        todos_contatos_db = mongo_repository.get_all_contacts()
        list_contacts = [contato for contato in todos_contatos_db]
        if (list_contacts):
            # dic_todos_contatos = helpers.add_total_contacts_by_type(list_contacts)
            return list_contacts, 200
        return 'Não há contatos ainda..', 200


class AgendaListarUmContato(Resource):
    """EXIBIR UM CONTATO POR ID - (ID É UMA STRING)"""
    def get(self, id):
        contato = mongo_repository.get_contact_by_id(id)
        if contato:
            return contato, 200
        return "Nao foi encontrado nenhum contato com esse ID", 404


class AgendaListarPorLetra(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""
    def get(self, letter):
        all_contacts_letter = mongo_repository.get_contacts_by_first_letter(letter)
        list_all_contacts_letter = [contato for contato in all_contacts_letter]
        if list_all_contacts_letter:
            return list_all_contacts_letter, 200
        else:
            return 'Nenhum contato encontrado', 404


class AgendaCadastrarContato(Resource):
    """CADASTRAR CONTATO"""
    def post(self):
        novo_contato = request.get_json()
        mongo_repository.register_contact(novo_contato)
        return "Cadastrado com sucesso", 201


class AgendaEditarContato(Resource):
    """EDITAR CONTATO POR ID - (ID É UMA STRING)"""
    def put(self, id):
        contato_editar = request.get_json()
        contato_editado = mongo_repository.update_contact(contato_editar, id)
        if contato_editado:
            return "Contato editado com sucesso", 201
        else:
            return "Não foi possível editar o contato", 500


class AgendaExcluirContato(Resource):
    """EXCLUIR CONTATO POR ID - (ID É UMA STRING)"""
    def delete(self, id):
        try:
            mongo_repository.soft_delete_contact(id)
            return "Removido com sucesso", 200
        except:
            return 'Não é possível excluir, contato não foi encontrado', 404


class AgendaCountPhonesByType(Resource):
    def get():
        pass
