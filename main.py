from flask import Flask
from flask_restful import Api
from flask_pydantic_spec import FlaskPydanticSpec
from controllers.agenda_controller import AgendaListarPorLetra, AgendaCadastrarContato, AgendaEditarContato, AgendaExcluirContato, AgendaListarTodos, AgendaListarUmContato, HelloWord


app = Flask(__name__)
api = Api(app)

spec = FlaskPydanticSpec('flask', title='API_AGENDA_LIONX')
spec.register(app)

api.add_resource(HelloWord, '/')
api.add_resource(AgendaListarTodos, '/contatos')
api.add_resource(AgendaListarPorLetra, '/contatos/<string:letra>')
api.add_resource(AgendaListarUmContato, '/contato/<string:id>')
api.add_resource(AgendaCadastrarContato, '/cadastrar-contato')
api.add_resource(AgendaEditarContato, '/editar-contato/<string:id>')
api.add_resource(AgendaExcluirContato, '/excluir-contato/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)
    # contato = consultar_contato_por_id('93b68bd5-20d4-4371-adab-0d935b9634cf')
    # a = consultar_contato_por_letra('v')
    # print(a)
    # dic = [contato for contato in a]
    # print(dic, 'este é o dic')
    # print(contato)
