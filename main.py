from src.routers.schedule.signature import RoutesSignature
from src.services.docs.api_specifications import DocsSpecifications

from flask import Flask

app = Flask(__name__)

routes = RoutesSignature()
routes.init_routes(app)

specs = DocsSpecifications()
specs.init_spec(app)

if __name__ == "__main__":
    app.run(debug=True)
