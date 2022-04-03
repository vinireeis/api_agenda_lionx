# Third party
from flask_pydantic_spec import FlaskPydanticSpec


class DocsSpecifications:
    @staticmethod
    def init_spec(app):
        spec = FlaskPydanticSpec('flask', title='API_AGENDA_LIONX')
        spec.register(app)
