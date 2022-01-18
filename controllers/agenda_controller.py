from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec
from flask_restful import Api, Resource
from pydantic import BaseModel
from app.services import querys_service
from typing import List, Optional

app = Flask(__name__)
api = Api(app)
spec = FlaskPydanticSpec('flask', title='API_AGENDA_LIONX')
spec.register(app)


class Contato(BaseModel):
    nome: Optional[str]
    telefone: List[dict[str, str]]
    email: str
    endereco: str


class HelloWord(Resource):
    """ESSA ROTA É OLA MUNDO"""
    def get(self):
        return "OLA MUNDOOO"


class AgendaListarTodos(Resource):
    """EXIBIR TODOS OS CONTATOS"""
    # @spec.validate(resp=Response(HTTP_200=Contato))
    def get(self):
        todos_contatos_db = querys_service.consultar_todos_contatos()
        dic_todos_contatos = [contato for contato in todos_contatos_db]
        if (dic_todos_contatos):
            return dic_todos_contatos, 200
        return 'Nenhum contato encontrado', 404


class AgendaListarUmContato(Resource):
    """EXIBIR UM CONTATO POR ID"""
    def get(self, id):
        try:
            contato = querys_service.consultar_contato_por_id(id)
            if (contato):
                return contato, 200
        except:
            return "Contato não encontrado", 404


class AgendaCadastrarContato(Resource):
    """CADASTRAR CONTATO"""
    def post(self):
        novo_contato = request.get_json()
        querys_service.cadastrar_um_contato(novo_contato)
        return "Cadastrado com sucesso", 201


class AgendaEditarContato(Resource):
    """EDITAR CONTATO POR ID"""
    def put(contato_editado, id):
        querys_service.editar_um_contato(contato_editado, id)
        return "Contato editado com sucesso", 201


class AgendaExcluirContato(Resource):
    """EXCLUIR CONTATO POR ID"""
    def delete(id):
        querys_service.remover_um_contato(id)
        return "Removido com sucesso", 200


class AgendaBuscarPorTermo(Resource):
    """BUSCAR CONTATO POR NOME"""
    pass


api.add_resource(HelloWord, '/')
api.add_resource(AgendaListarTodos, '/contatos')
api.add_resource(AgendaBuscarPorTermo, '/contatos/<string:termo>')
api.add_resource(AgendaListarUmContato, '/contato/<string:id>')
api.add_resource(AgendaCadastrarContato, '/cadastrar-contato')
api.add_resource(AgendaEditarContato, '/editar-contato/<int:id>')
api.add_resource(AgendaExcluirContato, '/excluir-contato/<int:id>')
