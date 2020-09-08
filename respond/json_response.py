from flask import jsonify, make_response, Response

from typing import Optional, Any
from http import HTTPStatus


class JSONResponse(object):

    @classmethod
    def _send_response(cls, status: int, data: Any, headers: Optional[dict] = None):
        """ Build and return the response """
        response: Response = make_response(jsonify(data), status)
        if headers:
            for k, v in headers.items():
                response.headers.set(k, v)
        return response

    @classmethod
    def continue_(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 100 CONTINUE """
        return cls._send_response(HTTPStatus.CONTINUE, data, headers)

    @classmethod
    def switching_protocols(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 101 SWITCHING_PROTOCOLS """
        return cls._send_response(HTTPStatus.SWITCHING_PROTOCOLS, data, headers)

    @classmethod
    def processing(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 102 PROCESSING """
        return cls._send_response(HTTPStatus.PROCESSING, data, headers)

    @classmethod
    def ok(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 200 OK """
        return cls._send_response(HTTPStatus.OK, data, headers)

    @classmethod
    def created(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 201 CREATED """
        return cls._send_response(HTTPStatus.CREATED, data, headers)

    @classmethod
    def accepted(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 202 ACCEPTED """
        return cls._send_response(HTTPStatus.ACCEPTED, data, headers)

    @classmethod
    def non_authoritative_information(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 203 NON_AUTHORITATIVE_INFORMATION """
        return cls._send_response(HTTPStatus.NON_AUTHORITATIVE_INFORMATION, data, headers)

    @classmethod
    def no_content(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 204 NO_CONTENT """
        return cls._send_response(HTTPStatus.NO_CONTENT, data, headers)

    @classmethod
    def reset_content(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 205 RESET_CONTENT """
        return cls._send_response(HTTPStatus.RESET_CONTENT, data, headers)

    @classmethod
    def partial_content(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 206 PARTIAL_CONTENT """
        return cls._send_response(HTTPStatus.PARTIAL_CONTENT, data, headers)

    @classmethod
    def multi_status(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 207 MULTI_STATUS """
        return cls._send_response(HTTPStatus.MULTI_STATUS, data, headers)

    @classmethod
    def already_reported(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 208 ALREADY_REPORTED """
        return cls._send_response(HTTPStatus.ALREADY_REPORTED, data, headers)

    @classmethod
    def im_used(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 226 IM_USED """
        return cls._send_response(HTTPStatus.IM_USED, data, headers)

    @classmethod
    def multiple_choices(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 300 MULTIPLE_CHOICES """
        return cls._send_response(HTTPStatus.MULTIPLE_CHOICES, data, headers)

    @classmethod
    def moved_permanently(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 301 MOVED_PERMANENTLY """
        return cls._send_response(HTTPStatus.MOVED_PERMANENTLY, data, headers)

    @classmethod
    def found(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 302 FOUND """
        return cls._send_response(HTTPStatus.FOUND, data, headers)

    @classmethod
    def see_other(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 303 SEE_OTHER """
        return cls._send_response(HTTPStatus.SEE_OTHER, data, headers)

    @classmethod
    def not_modified(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 304 NOT_MODIFIED """
        return cls._send_response(HTTPStatus.NOT_MODIFIED, data, headers)

    @classmethod
    def use_proxy(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 305 USE_PROXY """
        return cls._send_response(HTTPStatus.USE_PROXY, data, headers)

    @classmethod
    def temporary_redirect(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 307 TEMPORARY_REDIRECT """
        return cls._send_response(HTTPStatus.TEMPORARY_REDIRECT, data, headers)

    @classmethod
    def permanent_redirect(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 308 PERMANENT_REDIRECT """
        return cls._send_response(HTTPStatus.PERMANENT_REDIRECT, data, headers)

    @classmethod
    def bad_request(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 400 BAD_REQUEST """
        return cls._send_response(HTTPStatus.BAD_REQUEST, data, headers)

    @classmethod
    def unauthorized(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 401 UNAUTHORIZED """
        return cls._send_response(HTTPStatus.UNAUTHORIZED, data, headers)

    @classmethod
    def payment_required(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 402 PAYMENT_REQUIRED """
        return cls._send_response(HTTPStatus.PAYMENT_REQUIRED, data, headers)

    @classmethod
    def forbidden(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 403 FORBIDDEN """
        return cls._send_response(HTTPStatus.FORBIDDEN, data, headers)

    @classmethod
    def not_found(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 404 NOT_FOUND """
        return cls._send_response(HTTPStatus.NOT_FOUND, data, headers)

    @classmethod
    def method_not_allowed(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 405 METHOD_NOT_ALLOWED """
        return cls._send_response(HTTPStatus.METHOD_NOT_ALLOWED, data, headers)

    @classmethod
    def not_acceptable(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 406 NOT_ACCEPTABLE """
        return cls._send_response(HTTPStatus.NOT_ACCEPTABLE, data, headers)

    @classmethod
    def proxy_authentication_required(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 407 PROXY_AUTHENTICATION_REQUIRED """
        return cls._send_response(HTTPStatus.PROXY_AUTHENTICATION_REQUIRED, data, headers)

    @classmethod
    def request_timeout(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 408 REQUEST_TIMEOUT """
        return cls._send_response(HTTPStatus.REQUEST_TIMEOUT, data, headers)

    @classmethod
    def conflict(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 409 CONFLICT """
        return cls._send_response(HTTPStatus.CONFLICT, data, headers)

    @classmethod
    def gone(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 410 GONE """
        return cls._send_response(HTTPStatus.GONE, data, headers)

    @classmethod
    def length_required(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 411 LENGTH_REQUIRED """
        return cls._send_response(HTTPStatus.LENGTH_REQUIRED, data, headers)

    @classmethod
    def precondition_failed(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 412 PRECONDITION_FAILED """
        return cls._send_response(HTTPStatus.PRECONDITION_FAILED, data, headers)

    @classmethod
    def request_entity_too_large(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 413 REQUEST_ENTITY_TOO_LARGE """
        return cls._send_response(HTTPStatus.REQUEST_ENTITY_TOO_LARGE, data, headers)

    @classmethod
    def request_uri_too_long(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 414 REQUEST_URI_TOO_LONG """
        return cls._send_response(HTTPStatus.REQUEST_URI_TOO_LONG, data, headers)

    @classmethod
    def unsupported_media_type(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 415 UNSUPPORTED_MEDIA_TYPE """
        return cls._send_response(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, data, headers)

    @classmethod
    def requested_range_not_satisfiable(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 416 REQUESTED_RANGE_NOT_SATISFIABLE """
        return cls._send_response(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE, data, headers)

    @classmethod
    def expectation_failed(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 417 EXPECTATION_FAILED """
        return cls._send_response(HTTPStatus.EXPECTATION_FAILED, data, headers)

    @classmethod
    def im_a_teapot(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 418 IM_A_TEAPOT """
        return cls._send_response(418, data, headers)

    @classmethod
    def misdirected_request(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 421 MISDIRECTED_REQUEST """
        return cls._send_response(HTTPStatus.MISDIRECTED_REQUEST, data, headers)

    @classmethod
    def unprocessable_entity(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 422 UNPROCESSABLE_ENTITY """
        return cls._send_response(HTTPStatus.UNPROCESSABLE_ENTITY, data, headers)

    @classmethod
    def locked(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 423 LOCKED """
        return cls._send_response(HTTPStatus.LOCKED, data, headers)

    @classmethod
    def failed_dependency(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 424 FAILED_DEPENDENCY """
        return cls._send_response(HTTPStatus.FAILED_DEPENDENCY, data, headers)

    @classmethod
    def upgrade_required(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 426 UPGRADE_REQUIRED """
        return cls._send_response(HTTPStatus.UPGRADE_REQUIRED, data, headers)

    @classmethod
    def precondition_required(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 428 PRECONDITION_REQUIRED """
        return cls._send_response(HTTPStatus.PRECONDITION_REQUIRED, data, headers)

    @classmethod
    def too_many_requests(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 429 TOO_MANY_REQUESTS """
        return cls._send_response(HTTPStatus.TOO_MANY_REQUESTS, data, headers)

    @classmethod
    def request_header_fields_too_large(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 431 REQUEST_HEADER_FIELDS_TOO_LARGE """
        return cls._send_response(HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE, data, headers)

    @classmethod
    def unavailable_for_legal_reasons(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 451 UNAVAILABLE_FOR_LEGAL_REASONS """
        return cls._send_response(HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS, data, headers)

    @classmethod
    def internal_server_error(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 500 INTERNAL_SERVER_ERROR """
        return cls._send_response(HTTPStatus.INTERNAL_SERVER_ERROR, data, headers)

    @classmethod
    def not_implemented(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 501 NOT_IMPLEMENTED """
        return cls._send_response(HTTPStatus.NOT_IMPLEMENTED, data, headers)

    @classmethod
    def bad_gateway(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 502 BAD_GATEWAY """
        return cls._send_response(HTTPStatus.BAD_GATEWAY, data, headers)

    @classmethod
    def service_unavailable(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 503 SERVICE_UNAVAILABLE """
        return cls._send_response(HTTPStatus.SERVICE_UNAVAILABLE, data, headers)

    @classmethod
    def gateway_timeout(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 504 GATEWAY_TIMEOUT """
        return cls._send_response(HTTPStatus.GATEWAY_TIMEOUT, data, headers)

    @classmethod
    def http_version_not_supported(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 505 HTTP_VERSION_NOT_SUPPORTED """
        return cls._send_response(HTTPStatus.HTTP_VERSION_NOT_SUPPORTED, data, headers)

    @classmethod
    def variant_also_negotiates(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 506 VARIANT_ALSO_NEGOTIATES """
        return cls._send_response(HTTPStatus.VARIANT_ALSO_NEGOTIATES, data, headers)

    @classmethod
    def insufficient_storage(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 507 INSUFFICIENT_STORAGE """
        return cls._send_response(HTTPStatus.INSUFFICIENT_STORAGE, data, headers)

    @classmethod
    def loop_detected(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 508 LOOP_DETECTED """
        return cls._send_response(HTTPStatus.LOOP_DETECTED, data, headers)

    @classmethod
    def not_extended(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 510 NOT_EXTENDED """
        return cls._send_response(HTTPStatus.NOT_EXTENDED, data, headers)

    @classmethod
    def network_authentication_required(cls, data: Optional[Any] = "", headers: Optional[dict] = None):
        """ HTTP 511 NETWORK_AUTHENTICATION_REQUIRED """
        return cls._send_response(HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED, data, headers)