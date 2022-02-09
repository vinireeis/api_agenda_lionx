# from flask import request
from flask import request, Response
from logging import getLogger
from func.src.services.url.service import create_url_path

json = {
    'symbol': '6549PETR',
    'region': 'br'
}

log = getLogger()


def get_ticker_visual_identity():
    json_params = request.json
    url_path = create_url_path(json_params)
    # try:
    #     request.get_json(url_path)
    #     response = {
    #         'status': True,
    #         'logo_uri': url_path
    #         }
    #     return response
    # except Exception as e:
    #     log.error(str(e), exc_info=e)
    #     if resp.status_code == 400:
    #         response = {
    #             'status': False,
    #             'message': str(e)
    #             }
    #     return ''
        # return Response(
        #     json.dumps(response),
        #     mimetype="application/json",
        #     status=400)


if __name__ == '__main__':
    a = get_ticker_visual_identity(json)
    print(a)
