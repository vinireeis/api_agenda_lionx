from src.routers.schedule.router import (
    HelloWord,
    AgendaCadastrarContato,
    AgendaCountPhonesByType,
    AgendaEditarContato,
    AgendaExcluirContato,
    AgendaListarPorLetra,
    AgendaListarTodos,
    AgendaListarUmContato,
)

from flask_restful import Api


class RoutesSignature:
    @staticmethod
    def init_routes(app):
        api = Api(app)
        api.add_resource(HelloWord, "/")
        api.add_resource(AgendaListarTodos, "/contacts")
        api.add_resource(AgendaListarPorLetra, "/contacts/<string:letter>")
        api.add_resource(AgendaListarUmContato, "/contact/<string:id>")
        api.add_resource(AgendaCadastrarContato, "/register")
        api.add_resource(AgendaEditarContato, "/edit/<string:id>")
        api.add_resource(AgendaExcluirContato, "/delete/<string:id>")
        api.add_resource(AgendaCountPhonesByType, "/count")
