from flask import request
from flask_restful import Resource
from database import mongo_repository


class HelloWord(Resource):
    """ESSA É A ROTA DE BOAS-VINDAS"""
    def get(self):
        return "OLA MUNDOOO"


class AgendaListarTodos(Resource):
    """EXIBIR TODOS OS CONTATOS"""
    # @spec.validate(resp=Response(HTTP_200=Contato))
    def get(self):
        todos_contatos_db = mongo_repository.get_all_contacts()
        dic_todos_contatos = [contato for contato in todos_contatos_db]
        if (dic_todos_contatos):
            return dic_todos_contatos, 200
        return 'Não há contatos ainda..', 200


class AgendaListarUmContato(Resource):
    """EXIBIR UM CONTATO POR ID - (ID É UMA STRING)"""
    def get(self, id):
        contato = mongo_repository.get_contact_by_id(id)
        return contato, 200
        return "Nao foi encontrado nenhum contato com esse ID", 200


class AgendaListarPorLetra(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""
    def get(self, letra):
        consulta_contatos = mongo_repository.get_contacts_by_first_letter(letra)
        todos_contatos_com_letra = [contato for contato in consulta_contatos]
        if todos_contatos_com_letra:
            return todos_contatos_com_letra
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
        contato_excluir = mongo_repository.soft_delete_contact(id)
        if contato_excluir:
            return "Removido com sucesso", 200
        else:
            return 'Não é possível excluir, pois o contato não foi encontrado', 404
