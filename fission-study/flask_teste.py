import json
from flask import Flask, request, Response
from logging import getLogger
from func.src.services.treatment_url.service import create_url_path, check_if_url_is_valid

app = Flask(__name__)
log = getLogger()


@app.route('/')
def hello():
    return 'Hello world'


@app.route('/ticket')
def get_ticker_visual_identity():
    json_params = request.json
    url_path = create_url_path(json_params)
    try:
        check_if_url_is_valid(url_path)
        response = {
            'status': True,
            'logo_uri': url_path
            }
        return response
    except Exception as e:
        log.error(str(e), exc_info=e)
        response = {'status': False, 'message': str(e)}
        return Response(
            json.dumps(response),
            mimetype="application/json"
            )


if __name__ == '__main__':
    app.run(debug=True)
