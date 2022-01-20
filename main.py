from db.conexao_mongodb import BancoDeDadosMongo
from flask import Flask
from flask_restful import Api
from flask_pydantic_spec import FlaskPydanticSpec
from controllers.agenda_controller import AgendaBuscarPorLetra, AgendaCadastrarContato, AgendaEditarContato, AgendaExcluirContato, AgendaListarTodos, AgendaListarUmContato


app = Flask(__name__)
api = Api(app)

banco_instancia = BancoDeDadosMongo()

spec = FlaskPydanticSpec('flask', title='API_AGENDA_LIONX')
spec.register(app)


api.add_resource(AgendaBuscarPorLetra, '/contatos/<string:letra>')
api.add_resource(AgendaListarUmContato, '/contato/<string:id>')
api.add_resource(AgendaCadastrarContato, '/cadastrar-contato')
api.add_resource(AgendaEditarContato, '/editar-contato/<string:id>')
api.add_resource(AgendaExcluirContato, '/excluir-contato/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
    # contato = consultar_contato_por_id('93b68bd5-20d4-4371-adab-0d935b9634cf')
    # print(contato)
