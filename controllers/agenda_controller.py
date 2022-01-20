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
        return 'Não há contatos ainda..'


class AgendaListarUmContato(Resource):
    """EXIBIR UM CONTATO POR ID"""
    def get(self, id):
        try:
            contato = query_service.consultar_contato_por_id(id)
            return contato, 200
        except:
            return "Nao foi encontrado nenhum contato com essa ID", 404


class AgendaCadastrarContato(Resource):
    """CADASTRAR CONTATO"""
    def post(self):
        novo_contato = request.get_json()
        query_service.cadastrar_um_contato(novo_contato)
        return "Cadastrado com sucesso", 201


class AgendaEditarContato(Resource):
    """EDITAR CONTATO POR ID"""
    def put(self, id):
        contato_editado = request.get_json()
        query_service.editar_um_contato(contato_editado, id)
        return "Contato editado com sucesso", 201


class AgendaExcluirContato(Resource):
    """EXCLUIR CONTATO POR ID"""
    def delete(self, id):
        query_service.remover_um_contato(id)
        return "Removido com sucesso", 200


class AgendaBuscarPorLetra(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""
    def get(self, letra):
        pass
