from controllers.agenda_controller import app
from services.query_service import consultar_contato_por_id, cadastrar_um_contato, editar_um_contato, remover_um_contato


if __name__ == '__main__':
    app.run(debug=True)
    # contato = consultar_contato_por_id('93b68bd5-20d4-4371-adab-0d935b9634cf')
    # print(contato)
