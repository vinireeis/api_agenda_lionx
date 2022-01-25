from flask_restful import Api
from src.resources.resources import AgendaCadastrarContato, AgendaEditarContato, AgendaExcluirContato, AgendaListarPorLetra, AgendaListarTodos, AgendaListarUmContato, HelloWord


def init_api(app):
    api = Api(app)
    api.add_resource(HelloWord, '/')
    api.add_resource(AgendaListarTodos, '/contatos')
    api.add_resource(AgendaListarPorLetra, '/contatos/<string:letra>')
    api.add_resource(AgendaListarUmContato, '/contato/<string:id>')
    api.add_resource(AgendaCadastrarContato, '/cadastrar-contato')
    api.add_resource(AgendaEditarContato, '/editar-contato/<string:id>')
    api.add_resource(AgendaExcluirContato, '/excluir-contato/<string:id>')
