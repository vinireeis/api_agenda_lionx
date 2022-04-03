# Api Agenda Lionx
from src.routers.schedule.router import (
    CountPhonesByType,
    EditContact,
    HelloWord,
    ListAllContacts,
    ListContactById,
    ListContactsByLetters,
    RegisterContact,
    SoftDeleteContact
)

# Third party
from flask_restful import Api


class RoutesSignature:
    @staticmethod
    def init_routes(app):
        api = Api(app)
        api.add_resource(HelloWord, "/")
        api.add_resource(ListAllContacts, "/contacts")
        api.add_resource(ListContactsByLetters, "/contacts/<string:letters>")
        api.add_resource(ListContactById, "/contact/<string:id>")
        api.add_resource(RegisterContact, "/register")
        api.add_resource(EditContact, "/edit/<string:id>")
        api.add_resource(SoftDeleteContact, "/delete/<string:id>")
        api.add_resource(CountPhonesByType, "/count")
