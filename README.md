# jsonres

![Python package](https://github.com/Julian-Nash/jsonres/workflows/Python%20package/badge.svg?branch=master)

`jsonres` is a small, lightweight wrapper around Flask's `make_response` and `jsonify`, providing a fast and convenient
way to return JSON data with the right HTTP status code.

`jsonres` utilizes HTTP status code messages as methods in a declarative way, you simply call a static method 
such as `ok`, `not_found` or `internal_server_error` and optionally pass in the data you wish to return as JSON.

> Python v3.6 +

## Installation

```shell script
pip install jsonres
```

## Usage

Import the `jsonresonse` class

```py3
from jsonres import jsonresonse
```

You can now call one of many staticmethods of the class

Return a `200 OK` status code and a list

```py3
@app.route("/")
def example():
    """ Returns a list with an HTTP 200 OK status code """
    return jsonresonse.ok([1, 2, 3])
```

Return a `400 BAD REQUEST` status code and a dict

```py3
@app.route("/")
def example():
    """ Returns a dict with an HTTP 400 BAD REQUEST status code """
    return jsonresonse.bad_request({"message": "You did something wrong"})
```

Return a `500 INTERNAL SERVER ERROR` status code

```py3
@app.route("/")
def example():
    """ Returns an empty string with an HTTP 500 INTERNAL SERVER ERROR status code """
    return jsonresonse.bad_request()
```

Passing no data to the method returns an empty string

```py3
@app.route("/")
def ok():
    """ Return an empty HTTP 200 OK response """
    return jsonresonse.ok()
```

You can optionally pass in a headers dict if required

```py3
@app.route("/")
def example():
    """ Return a dict with custom headers """
    return jsonresonse.ok(data={"message": "ok"}, headers={"X-Custom-Header": "hello!"})
```

Taking a look in the Chrome developer tools, we can see our custom header:

```shell script
Content-Length: 17
Date: Sun, 03 May 2020 16:49:41 GMT
Content-Type: application/json
Server: Werkzeug/1.0.1 Python/3.8.2
X-Custom-Header: hello!
```

`jsonres` has methods for all HTTP status codes defined by the ietf - https://tools.ietf.org/html/rfc7231

Common status codes include, `404 NOT FOUND`, here being used in a Flask error handler

```py3
def handle_not_found_error(e):
    """ Handler for not found errors """
    app.logger.warning(e)
    return jsonresonse.not_found(data={"message": "Not found"})

app.register_error_handler(404, handle_not_found_error)
```

And `500 INTERNAL SERVER ERROR`

```py3
@app.route("/internal-server-error")
def internal_server_error():
    msg = {"message": "Whoops, we did something wrong"}
    return jsonresonse.internal_server_error(msg)
```

Visiting this URL in the browser returns

```shell script
{"message":"Whoops, we did something wrong"}
```

## Flask example

Here's a trivial example, showing `jsonres` in action

```py3
from flask import Flask

from jsonres import jsonresonse


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def ok():
        """ Return an empty HTTP 200 OK response """
        return jsonresonse.ok()

    @app.route("/dict")
    def d():
        """ Return a dict """
        return jsonresonse.ok({"message": "ok"})

    @app.route("/with-headers")
    def with_headers():
        """ Return a dict with custom headers """
        return jsonresonse.ok(
            data={"message": "ok"},
            headers={"X-Custom-Header": "hello!"}
        )

    @app.route("/bad-request")
    def bad_request():
        """ Return a 400 response with a dict """
        data = {"message": "You did something wrong"}
        return jsonresonse.bad_request(data=data)

    @app.route("/unauthorized")
    def unauthorized():
        return jsonresonse.unauthorized()

    @app.route("/internal-server-error")
    def internal_server_error():
        msg = {"message": "Whoops, we did something wrong"}
        return jsonresonse.internal_server_error(msg)

    @app.route("/empty-list")
    def ok_empty_list():
        """ Return an empty list """
        return jsonresonse.ok(data=[])

    @app.route("/empty-dict")
    def ok_empty_dict():
        """ Return an empty dict """
        return jsonresonse.ok(data={})

    def handle_not_found_error(e):
        """ Handler for not found errors """
        app.logger.warning(e)
        return jsonresonse.not_found(data={"message": "Not found"})

    def handle_internal_server_error(e):
        """ Handler for internal server errors """
        app.logger.error(e)
        return jsonresonse.internal_server_error()

    app.register_error_handler(404, handle_not_found_error)
    app.register_error_handler(500, handle_internal_server_error)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

```

## Methods available

**100 range (informational)**

| method | HTTP Status code |
| ------ | ---------------- |
| `continue` | `100 `|
| `switching_protocol` | `101 `|
| `processing` | `102 `|
| `early_hints` | `103 `|

**200 range (success)**

| method | HTTP Status code |
| ------ | ---------------- |
| `ok` | `200 `|
| `created` | `201 `|
| `accepted` | `202 `|
| `non_authoritative_information` | `203 `|
| `no_content` | `204 `|
| `reset_content` | `205 `|
| `partial_content` | `206 `|
| `multi_status` | `207 `|
| `already_reported` | `208 `|
| `im_used` | `226 `|

**300 range (redirection)**

| method | HTTP Status code |
| ------ | ---------------- |
| `multiple_choice` | `300 `|
| `moved_permanently` | `301 `|
| `found` | `302 `|
| `see_other` | `303 `|
| `not_modified` | `304 `|
| `use_proxy` | `305 `|
| `unused` | `306 `|
| `temporary_redirect` | `307 `|
| `permanent_redirect` | `308 `|

**400 range (client error)**

| method | HTTP Status code |
| ------ | ---------------- |
| `bad_request` | `400 `|
| `unauthorized` | `401 `|
| `payment_required` | `402 `|
| `forbidden` | `403 `|
| `not_found` | `404 `|
| `method_not_allowed` | `405 `|
| `not_acceptable` | `406 `|
| `proxy_authentication_required` | `407 `|
| `request_timeout` | `408 `|
| `conflict` | `409 `|
| `gone` | `410 `|
| `length_required` | `411 `|
| `precondition_failed` | `412 `|
| `payload_too_large` | `413 `|
| `uri_too_long` | `414 `|
| `unsupported_media_type` | `415 `|
| `requested_range_not_satisfiable` | `416 `|
| `expectation_failed` | `417 `|
| `im_a_teapot` | `418 `|
| `misdirected_request` | `421 `|
| `unprocessable_entity` | `422 `|
| `locked` | `423 `|
| `failed_dependency` | `424 `|
| `too_early` | `425 `|
| `upgrade_required` | `426 `|
| `precondition_required` | `428 `|
| `too_many_requests` | `429 `|
| `request_header_fields_too_large` | `431 `|
| `unavailable_for_legal_reasons` | `451 `|

**500 range (server error)**

| method | HTTP Status code |
| ------ | ---------------- |
| `internal_server_error` | `500 `|
| `not_implemented` | `501 `|
| `bad_gateway` | `502 `|
| `service_unavailable` | `503 `|
| `gateway_timeout` | `504 `|
| `http_version_not_supported` | `505 `|
| `variant_also_negotiates` | `506 `|
| `insufficient_storage` | `507 `|
| `loop_detected` | `508 `|
| `not_extended` | `510 `|
| `network_authentication_required` | `511 `|