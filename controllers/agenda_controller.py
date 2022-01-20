from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec
from flask_restful import Api, Resource
from services import query_service
from db.conexao_mongodb import BancoDeDadosMongo


app = Flask(__name__)
api = Api(app)
banco_instancia = BancoDeDadosMongo()
spec = FlaskPydanticSpec('flask', title='API_AGENDA_LIONX')
spec.register(app)


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


api.add_resource(HelloWord, '/')
api.add_resource(AgendaListarTodos, '/contatos')
api.add_resource(AgendaBuscarPorLetra, '/contatos/<string:letra>')
api.add_resource(AgendaListarUmContato, '/contato/<string:id>')
api.add_resource(AgendaCadastrarContato, '/cadastrar-contato')
api.add_resource(AgendaEditarContato, '/editar-contato/<string:id>')
api.add_resource(AgendaExcluirContato, '/excluir-contato/<string:id>')
