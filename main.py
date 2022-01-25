from flask import Flask
from src.resources.pydantic_api_specification import init_spec
from src.resources.routes import init_api


app = Flask(__name__)
init_api(app)
init_spec(app)


if __name__ == '__main__':
    app.run(debug=True)
