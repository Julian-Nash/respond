import json
import unittest

from flask import Flask
from jsonres import JSONResponse


def create_app():

    app = Flask(__name__)

    @app.route("/ok")
    def ok():
        """ Return an empty HTTP 200 OK response """
        return JSONResponse.ok()

    @app.route("/dict")
    def d():
        """ Return a dict """
        return JSONResponse.ok({"message": "ok"})

    @app.route("/list")
    def l():
        """ Return a list """
        return JSONResponse.ok([1, 2, 3])

    @app.route("/headers")
    def with_headers():
        """ Return a dict with custom headers """
        return JSONResponse.ok(
            data={"message": "ok"},
            headers={"X-Custom-Header": "hello!"}
        )

    @app.route("/bad-request")
    def bad_request():
        """ Return a 400 response with a dict """
        data = {"message": "You did something wrong"}
        return JSONResponse.bad_request(data=data)

    @app.route("/unauthorized")
    def unauthorized():
        return JSONResponse.unauthorized()

    @app.route("/internal-server-error")
    def internal_server_error():
        msg = {"message": "Whoops, we did something wrong"}
        return JSONResponse.internal_server_error(msg)

    @app.route("/empty-list")
    def ok_empty_list():
        """ Return an empty list """
        return JSONResponse.ok(data=[])

    @app.route("/empty-dict")
    def ok_empty_dict():
        """ Return an empty dict """
        return JSONResponse.ok(data={})

    def handle_not_found_error(e):
        """ Handler for not found errors """
        app.logger.warning(e)
        return JSONResponse.not_found(data={"message": "Not found"})

    def handle_internal_server_error(e):
        """ Handler for internal server errors """
        app.logger.error(e)
        return JSONResponse.internal_server_error()

    app.register_error_handler(404, handle_not_found_error)
    app.register_error_handler(500, handle_internal_server_error)

    return app


class TestJSONResponse(unittest.TestCase):

    def setUp(self) -> None:
        app = create_app()
        self.test_client = app.test_client()

    def test_ok_status_code(self):
        url = "/ok"
        r = self.test_client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_ok_content(self):
        url = "/ok"
        r = self.test_client.get(url)
        self.assertEqual(r.data, b'""\n')

    def test_returns_dict(self):
        url = "/dict"
        expected = {"message": "ok"}
        r = self.test_client.get(url)
        self.assertEqual(json.loads(r.data), expected)

    def test_returns_list(self):
        url = "/list"
        expected = [1, 2, 3]
        r = self.test_client.get(url)
        self.assertEqual(json.loads(r.data), expected)

    def test_custom_header(self):
        url = "/headers"
        r = self.test_client.get(url)
        self.assertEqual(r.headers.get("X-Custom-Header"), "hello!")
