import requests


def validate_url_params(params_dict):
    if params_dict['region'].lower() == 'br':
        symbol_slice = params_dict['symbol']
        params_dict.update(symbol=symbol_slice[:4])
        return params_dict
    return params_dict


def create_url_path(params):
    dict_params = validate_url_params(params)
    url_path = f"https://sigame-companies-logo.s3.sa-east-1.amazonaws.com/{dict_params['region']}/{dict_params['symbol']}.png"
    return url_path


def status_200():
    return True


def status_400():
    raise Exception('Bad Request', 400)


def status_403():
    raise Exception('Bad Request', 403)


def check_if_url_is_valid(url_path):
    response_status_code = requests.get(url_path).status_code
    response = {
        200: status_200,
        400: status_400,
        403: status_403
    }
    if response_status_code not in response:
        raise Exception
    return response.get(response_status_code)()






if __name__ == '__main__':
    json = {
        'symbol': '1231PETR',
        'region': 'br'
    }
    a = validate_url_params(json)
