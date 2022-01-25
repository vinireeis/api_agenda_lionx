from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec
from flask_restful import Api, Resource
from src.database.mongo_repository import BancoDeDadosMongo


app = Flask(__name__)
api = Api(app)
spec = FlaskPydanticSpec('flask', title='API_AGENDA_LIONX')
spec.register(app)
banco = BancoDeDadosMongo().init_bd()


class HelloWord(Resource):
    """ESSA ROTA É OLA MUNDO"""
    def get(self):
        return "OLA MUNDOOO"


class AgendaListarTodos(Resource):
    """EXIBIR TODOS OS CONTATOS"""
    # @spec.validate(resp=Response(HTTP_200=Contato))
    def get(self):
        todos_contatos_db = repository.consultar_todos_contatos()
        dic_todos_contatos = [contato for contato in todos_contatos_db]
        if (dic_todos_contatos):
            return dic_todos_contatos, 200
        return 'Não há contatos ainda..', 200


class AgendaListarUmContato(Resource):
    """EXIBIR UM CONTATO POR ID - (ID É UMA STRING)"""
    def get(self, id):
        contato = repository.consultar_contato_por_id(id)
        return contato, 200
        return "Nao foi encontrado nenhum contato com esse ID", 200


class AgendaListarPorLetra(Resource):
    """BUSCAR CONTATO PELA PRIMEIRA LETRA DO NOME"""
    def get(self, letra):
        consulta_contatos = query_service.consultar_contato_por_letra(letra)
        todos_contatos_com_letra = [contato for contato in consulta_contatos]
        if todos_contatos_com_letra:
            return todos_contatos_com_letra
        else:
            return 'Nenhum contato encontrado', 404


class AgendaCadastrarContato(Resource):
    """CADASTRAR CONTATO"""
    def post(self):
        novo_contato = request.get_json()
        repository.cadastrar_um_contato(novo_contato)
        return "Cadastrado com sucesso", 201


class AgendaEditarContato(Resource):
    """EDITAR CONTATO POR ID - (ID É UMA STRING)"""
    def put(self, id):
        contato_editar = request.get_json()
        contato_editado = query_service.editar_um_contato(contato_editar, id)
        if contato_editado:
            return "Contato editado com sucesso", 201
        else:
            return "Não foi possível editar o contato", 500


class AgendaExcluirContato(Resource):
    """EXCLUIR CONTATO POR ID - (ID É UMA STRING)"""
    def delete(self, id):
        contato_excluir = query_service.remover_um_contato(id)
        if contato_excluir:
            return "Removido com sucesso", 200
        else:
            return 'Não é possível excluir, pois o contato não foi encontrado', 404
