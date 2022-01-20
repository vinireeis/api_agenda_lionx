from flask import request
from flask_restful import Resource
from services import query_service


class HelloWord(Resource):
    """ESSA ROTA É OLA MUNDO"""
    def get(self):
        return "OLA MUNDOOO"


class AgendaListarTodos(Resource):
    """EXIBIR TODOS OS CONTATOS"""
    # @spec.validate(resp=Response(HTTP_200=Contato))
    def get(self):
        todos_contatos_db = query_service.consultar_todos_contatos()
        dic_todos_contatos = [contato for contato in todos_contatos_db]
        if (dic_todos_contatos):
            return dic_todos_contatos, 200
        return 'Não há contatos ainda..', 200


class AgendaListarUmContato(Resource):
    """EXIBIR UM CONTATO POR ID"""
    def get(self, id):
        contato = query_service.consultar_contato_por_id(id)
        if contato:
            return contato, 200
        return "Nao foi encontrado nenhum contato com esse ID", 200


class AgendaListarPorLetra(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""
    def get(self, letra):
        consulta_contatos = query_service.consultar_contato_por_letra(letra)
        if consulta_contatos:
            todos_contatos_com_letra = [contato for contato in consulta_contatos]
            return todos_contatos_com_letra
        else:
            return 'Nenhum contato encontrado', 404


class AgendaCadastrarContato(Resource):
    """CADASTRAR CONTATO"""
    def post(self):
        novo_contato = request.get_json()
        query_service.cadastrar_um_contato(novo_contato)
        return "Cadastrado com sucesso", 201


class AgendaEditarContato(Resource):
    """EDITAR CONTATO POR ID"""
    def put(self, id):
        contato_editar = request.get_json()
        contato_editado = query_service.editar_um_contato(contato_editar, id)
        if contato_editado:
            return "Contato editado com sucesso", 201
        else:
            return "Não foi possível editar o contato", 500


class AgendaExcluirContato(Resource):
    """EXCLUIR CONTATO POR ID"""
    def delete(self, id):
        contato_excluir = query_service.remover_um_contato(id)
        if contato_excluir:
            return "Removido com sucesso", 200
        else:
            return 'Não é possível excluir, pois o contato não foi encontrado', 404
