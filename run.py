from flask import Flask
from src.routers.routes import Routes
from src.services.api_specifications import DocsSpecifications


app = Flask(__name__)

routes = Routes()
routes.init_routes(app)

specs = DocsSpecifications()
specs.init_spec(app)


if __name__ == '__main__':
    app.run(debug=True)
