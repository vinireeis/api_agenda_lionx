from flask_restful import Api
from src.resources.resources import AgendaCadastrarContato, AgendaCountPhonesByType, AgendaEditarContato, AgendaExcluirContato, AgendaListarPorLetra, AgendaListarTodos, AgendaListarUmContato, HelloWord


def init_api(app):
    api = Api(app)
    api.add_resource(HelloWord, '/')
    api.add_resource(AgendaListarTodos, '/contatos')
    api.add_resource(AgendaListarPorLetra, '/contatos/<string:letter>')
    api.add_resource(AgendaListarUmContato, '/contato/<string:id>')
    api.add_resource(AgendaCadastrarContato, '/cadastrar')
    api.add_resource(AgendaEditarContato, '/editar/<string:id>')
    api.add_resource(AgendaExcluirContato, '/excluir/<string:id>')
    api.add_resource(AgendaCountPhonesByType, '/count')
