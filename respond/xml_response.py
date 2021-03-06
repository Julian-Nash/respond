from .abs_http_response import HTTPResponse

from flask import make_response, Response

from typing import Optional, Any


class XMLResponse(HTTPResponse):

    @classmethod
    def _make_response(cls, status: int, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ Returns an XML response """
        response: Response = make_response(data if data is not None else "", status)
        response.headers.set("Content-Type", "text/xml; charset=utf-8")
        if headers:
            for k, v in headers.items():
                response.headers.set(k, v)
        return response
