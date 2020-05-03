from typing import Optional, Union

from flask import make_response, jsonify, Response
from httpz import HTTPStatusCodeEnum as HTTPStatusCode


class JSONResponse(object):
    """ Class for returning JSON responses """

    _default_data = ""

    @classmethod
    def _send_response(
            cls,
            status_code: int,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ Builds and returns a flask Response """
        resp: Response = make_response(jsonify(data or cls._default_data), status_code)
        if headers:
            resp.headers.update(**headers)
        return resp

    @classmethod
    def continue_(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 100 Continue """
        return cls._send_response(HTTPStatusCode.CONTINUE.value, data, headers)

    @classmethod
    def switching_protocol(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 101 Switching Protocol """
        return cls._send_response(HTTPStatusCode.SWITCHING_PROTOCOL.value, data, headers)

    @classmethod
    def processing(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 102 Processing """
        return cls._send_response(HTTPStatusCode.PROCESSING.value, data, headers)

    @classmethod
    def early_hints(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 103 Early Hints """
        return cls._send_response(HTTPStatusCode.EARLY_HINTS.value, data, headers)

    @classmethod
    def ok(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 200 OK """
        return cls._send_response(HTTPStatusCode.OK.value, data, headers)

    @classmethod
    def created(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 201 Created """
        return cls._send_response(HTTPStatusCode.CREATED.value, data, headers)

    @classmethod
    def accepted(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 202 Accepted """
        return cls._send_response(HTTPStatusCode.ACCEPTED.value, data, headers)

    @classmethod
    def non_authoritative_information(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 203 Non-Authoritative Information """
        return cls._send_response(HTTPStatusCode.NON_AUTHORITATIVE_INFORMATION.value, data, headers)

    @classmethod
    def no_content(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 204 No Content """
        return cls._send_response(HTTPStatusCode.NO_CONTENT.value, data, headers)

    @classmethod
    def reset_content(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 205 Reset Content """
        return cls._send_response(HTTPStatusCode.RESET_CONTENT.value, data, headers)

    @classmethod
    def partial_content(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 206 Partial Content """
        return cls._send_response(HTTPStatusCode.PARTIAL_CONTENT.value, data, headers)

    @classmethod
    def multi_status(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 207 Multi-Status """
        return cls._send_response(HTTPStatusCode.MULTI_STATUS.value, data, headers)

    @classmethod
    def already_reported(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 208 Already Reported """
        return cls._send_response(HTTPStatusCode.ALREADY_REPORTED.value, data, headers)

    @classmethod
    def im_used(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 226 IM Used """
        return cls._send_response(HTTPStatusCode.IM_USED.value, data, headers)

    @classmethod
    def multiple_choice(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 300 Multiple Choice """
        return cls._send_response(HTTPStatusCode.MULTIPLE_CHOICE.value, data, headers)

    @classmethod
    def moved_permanently(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 301 Moved Permanently """
        return cls._send_response(HTTPStatusCode.MOVED_PERMANENTLY.value, data, headers)

    @classmethod
    def found(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 302 Found """
        return cls._send_response(HTTPStatusCode.FOUND.value, data, headers)

    @classmethod
    def see_other(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 303 See Other """
        return cls._send_response(HTTPStatusCode.SEE_OTHER.value, data, headers)

    @classmethod
    def not_modified(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 304 Not Modified """
        return cls._send_response(HTTPStatusCode.NOT_MODIFIED.value, data, headers)

    @classmethod
    def use_proxy(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 305 Use Proxy """
        return cls._send_response(HTTPStatusCode.USE_PROXY.value, data, headers)

    @classmethod
    def unused(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 306 Unused """
        return cls._send_response(HTTPStatusCode.UNUSED.value, data, headers)

    @classmethod
    def temporary_redirect(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 307 Temporary Redirect """
        return cls._send_response(HTTPStatusCode.TEMPORARY_REDIRECT.value, data, headers)

    @classmethod
    def permanent_redirect(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 308 Permanent Redirect """
        return cls._send_response(HTTPStatusCode.PERMANENT_REDIRECT.value, data, headers)

    @classmethod
    def bad_request(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 400 Bad Request """
        return cls._send_response(HTTPStatusCode.BAD_REQUEST.value, data, headers)

    @classmethod
    def unauthorized(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 401 Unauthorized """
        return cls._send_response(HTTPStatusCode.UNAUTHORIZED.value, data, headers)

    @classmethod
    def payment_required(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 402 Payment Required """
        return cls._send_response(HTTPStatusCode.PAYMENT_REQUIRED.value, data, headers)

    @classmethod
    def forbidden(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 403 Forbidden """
        return cls._send_response(HTTPStatusCode.FORBIDDEN.value, data, headers)

    @classmethod
    def not_found(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 404 Not Found """
        return cls._send_response(HTTPStatusCode.NOT_FOUND.value, data, headers)

    @classmethod
    def method_not_allowed(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 405 Method Not Allowed """
        return cls._send_response(HTTPStatusCode.METHOD_NOT_ALLOWED.value, data, headers)

    @classmethod
    def not_acceptable(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 406 Not Acceptable """
        return cls._send_response(HTTPStatusCode.NOT_ACCEPTABLE.value, data, headers)

    @classmethod
    def proxy_authentication_required(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 407 Proxy Authentication Required """
        return cls._send_response(HTTPStatusCode.PROXY_AUTHENTICATION_REQUIRED.value, data, headers)

    @classmethod
    def request_timeout(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 408 Request Timeout """
        return cls._send_response(HTTPStatusCode.REQUEST_TIMEOUT.value, data, headers)

    @classmethod
    def conflict(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 409 Conflict """
        return cls._send_response(HTTPStatusCode.CONFLICT.value, data, headers)

    @classmethod
    def gone(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 410 Gone """
        return cls._send_response(HTTPStatusCode.GONE.value, data, headers)

    @classmethod
    def length_required(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 411 Length Required """
        return cls._send_response(HTTPStatusCode.LENGTH_REQUIRED.value, data, headers)

    @classmethod
    def precondition_failed(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 412 Precondition Failed """
        return cls._send_response(HTTPStatusCode.PRECONDITION_FAILED.value, data, headers)

    @classmethod
    def payload_too_large(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 413 Payload Too Large """
        return cls._send_response(HTTPStatusCode.PAYLOAD_TOO_LARGE.value, data, headers)

    @classmethod
    def uri_too_long(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 414 URI Too Long """
        return cls._send_response(HTTPStatusCode.URI_TOO_LONG.value, data, headers)

    @classmethod
    def unsupported_media_type(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 415 Unsupported Media Type """
        return cls._send_response(HTTPStatusCode.UNSUPPORTED_MEDIA_TYPE.value, data, headers)

    @classmethod
    def requested_range_not_satisfiable(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 416 Range Not Satisfiable """
        return cls._send_response(HTTPStatusCode.REQUESTED_RANGE_NOT_SATISFIABLE.value, data, headers)

    @classmethod
    def expectation_failed(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 417 Expectation Failed """
        return cls._send_response(HTTPStatusCode.EXPECTATION_FAILED.value, data, headers)

    @classmethod
    def im_a_teapot(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 418 I'm a teapot """
        return cls._send_response(HTTPStatusCode.IM_A_TEAPOT.value, data, headers)

    @classmethod
    def misdirected_request(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 421 Misdirected Request """
        return cls._send_response(HTTPStatusCode.MISDIRECTED_REQUEST.value, data, headers)

    @classmethod
    def unprocessable_entity(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 422 Unprocessable Entity """
        return cls._send_response(HTTPStatusCode.UNPROCESSABLE_ENTITY.value, data, headers)

    @classmethod
    def locked(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 423 Locked """
        return cls._send_response(HTTPStatusCode.LOCKED.value, data, headers)

    @classmethod
    def failed_dependency(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 424 Failed Dependency """
        return cls._send_response(HTTPStatusCode.FAILED_DEPENDENCY.value, data, headers)

    @classmethod
    def too_early(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 425 Too Early """
        return cls._send_response(HTTPStatusCode.TOO_EARLY.value, data, headers)

    @classmethod
    def upgrade_required(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 426 Upgrade Required """
        return cls._send_response(HTTPStatusCode.UPGRADE_REQUIRED.value, data, headers)

    @classmethod
    def precondition_required(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 428 Precondition Required """
        return cls._send_response(HTTPStatusCode.PRECONDITION_REQUIRED.value, data, headers)

    @classmethod
    def too_many_requests(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 429 Too Many Requests """
        return cls._send_response(HTTPStatusCode.TOO_MANY_REQUESTS.value, data, headers)

    @classmethod
    def request_header_fields_too_large(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 431 Request Header Fields Too Large """
        return cls._send_response(HTTPStatusCode.REQUEST_HEADER_FIELDS_TOO_LARGE.value, data, headers)

    @classmethod
    def unavailable_for_legal_reasons(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 451 Unavailable For Legal Reasons """
        return cls._send_response(HTTPStatusCode.UNAVAILABLE_FOR_LEGAL_REASONS.value, data, headers)

    @classmethod
    def internal_server_error(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 500 Internal Server Error """
        return cls._send_response(HTTPStatusCode.INTERNAL_SERVER_ERROR.value, data, headers)

    @classmethod
    def not_implemented(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 501 Not Implemented """
        return cls._send_response(HTTPStatusCode.NOT_IMPLEMENTED.value, data, headers)

    @classmethod
    def bad_gateway(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 502 Bad Gateway """
        return cls._send_response(HTTPStatusCode.BAD_GATEWAY.value, data, headers)

    @classmethod
    def service_unavailable(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 503 Service Unavailable """
        return cls._send_response(HTTPStatusCode.SERVICE_UNAVAILABLE.value, data, headers)

    @classmethod
    def gateway_timeout(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 504 Gateway Timeout """
        return cls._send_response(HTTPStatusCode.GATEWAY_TIMEOUT.value, data, headers)

    @classmethod
    def http_version_not_supported(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 505 HTTP Version Not Supported """
        return cls._send_response(HTTPStatusCode.HTTP_VERSION_NOT_SUPPORTED.value, data, headers)

    @classmethod
    def variant_also_negotiates(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 506 Variant Also Negotiates """
        return cls._send_response(HTTPStatusCode.VARIANT_ALSO_NEGOTIATES.value, data, headers)

    @classmethod
    def insufficient_storage(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 507 Insufficient Storage """
        return cls._send_response(HTTPStatusCode.INSUFFICIENT_STORAGE.value, data, headers)

    @classmethod
    def loop_detected(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 508 Loop Detected """
        return cls._send_response(HTTPStatusCode.LOOP_DETECTED.value, data, headers)

    @classmethod
    def not_extended(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 510 Not Extended """
        return cls._send_response(HTTPStatusCode.NOT_EXTENDED.value, data, headers)

    @classmethod
    def network_authentication_required(
            cls,
            data: Optional[Union[str, int, bool, list, dict, None]] = None,
            headers: Optional[dict] = None) -> Response:
        """ HTTP 511 Network Authentication Required """
        return cls._send_response(HTTPStatusCode.NETWORK_AUTHENTICATION_REQUIRED.value, data, headers)
