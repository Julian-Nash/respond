import json
import unittest

from .application import create_app


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
