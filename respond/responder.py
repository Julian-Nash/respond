from .json_response import JSONResponse
from .xml_response import XMLResponse
from .text_response import TextResponse


class Responder(object):
    """ Responder class for quick access to JSON, XML and text response classes """

    json: JSONResponse = JSONResponse
    xml: XMLResponse = XMLResponse
    text: JSONResponse = TextResponse
