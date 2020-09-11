from .json_response import JSONResponse
from .xml_response import XMLResponse
from .text_response import TextResponse


class Responder(object):
    """ Responder class for quick access to JSON, XML and text response classes

    Example usage:
        Send a JSON response:
            Responder.json.ok(["some", "json", "data"])  # Returns the data as JSON with an HTTP 200 OK status
            Responder.json.bad_request()  # Returns an empty JSON string with an HTTP 400 BAD REQUEST status
        Send a text response:
            Responder.text.ok("some text")
    """

    json: JSONResponse = JSONResponse
    xml: XMLResponse = XMLResponse
    text: JSONResponse = TextResponse
