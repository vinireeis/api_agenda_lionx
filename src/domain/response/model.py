# Standards
from json import dumps
from typing import Any

# Third party
from flask import Response


class ResponseBuilder:
    @staticmethod
    def response_http(success: bool, status: int, message: str = None, result: Any = None) -> Response:
        response_model = {
            "result": result,
            "message": message,
            "success": success,
        }
        response_http = Response(dumps(response_model), status=status, mimetype="application/json")
        return response_http
