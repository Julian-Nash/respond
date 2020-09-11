from typing import Optional, Any
from http import HTTPStatus
import abc


class HTTPResponse(abc.ABC):
    """ HTTPResponse abstract base class """

    @classmethod
    @abc.abstractmethod
    def _make_response(cls, status: int, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        raise NotImplementedError
    
    @classmethod
    def continue_(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 100 CONTINUE """
        return cls._make_response(HTTPStatus.CONTINUE, data, headers, **kwargs)

    @classmethod
    def switching_protocols(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 101 SWITCHING_PROTOCOLS """
        return cls._make_response(HTTPStatus.SWITCHING_PROTOCOLS, data, headers, **kwargs)

    @classmethod
    def processing(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 102 PROCESSING """
        return cls._make_response(HTTPStatus.PROCESSING, data, headers, **kwargs)

    @classmethod
    def ok(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 200 OK """
        return cls._make_response(HTTPStatus.OK, data, headers, **kwargs)

    @classmethod
    def created(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 201 CREATED """
        return cls._make_response(HTTPStatus.CREATED, data, headers, **kwargs)

    @classmethod
    def accepted(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 202 ACCEPTED """
        return cls._make_response(HTTPStatus.ACCEPTED, data, headers, **kwargs)

    @classmethod
    def non_authoritative_information(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 203 NON_AUTHORITATIVE_INFORMATION """
        return cls._make_response(HTTPStatus.NON_AUTHORITATIVE_INFORMATION, data, headers, **kwargs)

    @classmethod
    def no_content(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 204 NO_CONTENT """
        return cls._make_response(HTTPStatus.NO_CONTENT, data, headers, **kwargs)

    @classmethod
    def reset_content(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 205 RESET_CONTENT """
        return cls._make_response(HTTPStatus.RESET_CONTENT, data, headers, **kwargs)

    @classmethod
    def partial_content(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 206 PARTIAL_CONTENT """
        return cls._make_response(HTTPStatus.PARTIAL_CONTENT, data, headers, **kwargs)

    @classmethod
    def multi_status(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 207 MULTI_STATUS """
        return cls._make_response(HTTPStatus.MULTI_STATUS, data, headers, **kwargs)

    @classmethod
    def already_reported(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 208 ALREADY_REPORTED """
        return cls._make_response(HTTPStatus.ALREADY_REPORTED, data, headers, **kwargs)

    @classmethod
    def im_used(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 226 IM_USED """
        return cls._make_response(HTTPStatus.IM_USED, data, headers, **kwargs)

    @classmethod
    def multiple_choices(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 300 MULTIPLE_CHOICES """
        return cls._make_response(HTTPStatus.MULTIPLE_CHOICES, data, headers, **kwargs)

    @classmethod
    def moved_permanently(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 301 MOVED_PERMANENTLY """
        return cls._make_response(HTTPStatus.MOVED_PERMANENTLY, data, headers, **kwargs)

    @classmethod
    def found(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 302 FOUND """
        return cls._make_response(HTTPStatus.FOUND, data, headers, **kwargs)

    @classmethod
    def see_other(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 303 SEE_OTHER """
        return cls._make_response(HTTPStatus.SEE_OTHER, data, headers, **kwargs)

    @classmethod
    def not_modified(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 304 NOT_MODIFIED """
        return cls._make_response(HTTPStatus.NOT_MODIFIED, data, headers, **kwargs)

    @classmethod
    def use_proxy(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 305 USE_PROXY """
        return cls._make_response(HTTPStatus.USE_PROXY, data, headers, **kwargs)

    @classmethod
    def temporary_redirect(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 307 TEMPORARY_REDIRECT """
        return cls._make_response(HTTPStatus.TEMPORARY_REDIRECT, data, headers, **kwargs)

    @classmethod
    def permanent_redirect(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 308 PERMANENT_REDIRECT """
        return cls._make_response(HTTPStatus.PERMANENT_REDIRECT, data, headers, **kwargs)

    @classmethod
    def bad_request(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 400 BAD_REQUEST """
        return cls._make_response(HTTPStatus.BAD_REQUEST, data, headers, **kwargs)

    @classmethod
    def unauthorized(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 401 UNAUTHORIZED """
        return cls._make_response(HTTPStatus.UNAUTHORIZED, data, headers, **kwargs)

    @classmethod
    def payment_required(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 402 PAYMENT_REQUIRED """
        return cls._make_response(HTTPStatus.PAYMENT_REQUIRED, data, headers, **kwargs)

    @classmethod
    def forbidden(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 403 FORBIDDEN """
        return cls._make_response(HTTPStatus.FORBIDDEN, data, headers, **kwargs)

    @classmethod
    def not_found(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 404 NOT_FOUND """
        return cls._make_response(HTTPStatus.NOT_FOUND, data, headers, **kwargs)

    @classmethod
    def method_not_allowed(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 405 METHOD_NOT_ALLOWED """
        return cls._make_response(HTTPStatus.METHOD_NOT_ALLOWED, data, headers, **kwargs)

    @classmethod
    def not_acceptable(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 406 NOT_ACCEPTABLE """
        return cls._make_response(HTTPStatus.NOT_ACCEPTABLE, data, headers, **kwargs)

    @classmethod
    def proxy_authentication_required(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 407 PROXY_AUTHENTICATION_REQUIRED """
        return cls._make_response(HTTPStatus.PROXY_AUTHENTICATION_REQUIRED, data, headers, **kwargs)

    @classmethod
    def request_timeout(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 408 REQUEST_TIMEOUT """
        return cls._make_response(HTTPStatus.REQUEST_TIMEOUT, data, headers, **kwargs)

    @classmethod
    def conflict(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 409 CONFLICT """
        return cls._make_response(HTTPStatus.CONFLICT, data, headers, **kwargs)

    @classmethod
    def gone(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 410 GONE """
        return cls._make_response(HTTPStatus.GONE, data, headers, **kwargs)

    @classmethod
    def length_required(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 411 LENGTH_REQUIRED """
        return cls._make_response(HTTPStatus.LENGTH_REQUIRED, data, headers, **kwargs)

    @classmethod
    def precondition_failed(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 412 PRECONDITION_FAILED """
        return cls._make_response(HTTPStatus.PRECONDITION_FAILED, data, headers, **kwargs)

    @classmethod
    def request_entity_too_large(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 413 REQUEST_ENTITY_TOO_LARGE """
        return cls._make_response(HTTPStatus.REQUEST_ENTITY_TOO_LARGE, data, headers, **kwargs)

    @classmethod
    def request_uri_too_long(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 414 REQUEST_URI_TOO_LONG """
        return cls._make_response(HTTPStatus.REQUEST_URI_TOO_LONG, data, headers, **kwargs)

    @classmethod
    def unsupported_media_type(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 415 UNSUPPORTED_MEDIA_TYPE """
        return cls._make_response(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, data, headers, **kwargs)

    @classmethod
    def requested_range_not_satisfiable(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 416 REQUESTED_RANGE_NOT_SATISFIABLE """
        return cls._make_response(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE, data, headers, **kwargs)

    @classmethod
    def expectation_failed(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 417 EXPECTATION_FAILED """
        return cls._make_response(HTTPStatus.EXPECTATION_FAILED, data, headers, **kwargs)

    @classmethod
    def im_a_teapot(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 418 IM_A_TEAPOT """
        return cls._make_response(418, data, headers, **kwargs)

    @classmethod
    def misdirected_request(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 421 MISDIRECTED_REQUEST """
        return cls._make_response(HTTPStatus.MISDIRECTED_REQUEST, data, headers, **kwargs)

    @classmethod
    def unprocessable_entity(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 422 UNPROCESSABLE_ENTITY """
        return cls._make_response(HTTPStatus.UNPROCESSABLE_ENTITY, data, headers, **kwargs)

    @classmethod
    def locked(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 423 LOCKED """
        return cls._make_response(HTTPStatus.LOCKED, data, headers, **kwargs)

    @classmethod
    def failed_dependency(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 424 FAILED_DEPENDENCY """
        return cls._make_response(HTTPStatus.FAILED_DEPENDENCY, data, headers, **kwargs)

    @classmethod
    def upgrade_required(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 426 UPGRADE_REQUIRED """
        return cls._make_response(HTTPStatus.UPGRADE_REQUIRED, data, headers, **kwargs)

    @classmethod
    def precondition_required(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 428 PRECONDITION_REQUIRED """
        return cls._make_response(HTTPStatus.PRECONDITION_REQUIRED, data, headers, **kwargs)

    @classmethod
    def too_many_requests(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 429 TOO_MANY_REQUESTS """
        return cls._make_response(HTTPStatus.TOO_MANY_REQUESTS, data, headers, **kwargs)

    @classmethod
    def request_header_fields_too_large(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 431 REQUEST_HEADER_FIELDS_TOO_LARGE """
        return cls._make_response(HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE, data, headers, **kwargs)

    @classmethod
    def unavailable_for_legal_reasons(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 451 UNAVAILABLE_FOR_LEGAL_REASONS """
        return cls._make_response(HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS, data, headers, **kwargs)

    @classmethod
    def internal_server_error(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 500 INTERNAL_SERVER_ERROR """
        return cls._make_response(HTTPStatus.INTERNAL_SERVER_ERROR, data, headers, **kwargs)

    @classmethod
    def not_implemented(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 501 NOT_IMPLEMENTED """
        return cls._make_response(HTTPStatus.NOT_IMPLEMENTED, data, headers, **kwargs)

    @classmethod
    def bad_gateway(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 502 BAD_GATEWAY """
        return cls._make_response(HTTPStatus.BAD_GATEWAY, data, headers, **kwargs)

    @classmethod
    def service_unavailable(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 503 SERVICE_UNAVAILABLE """
        return cls._make_response(HTTPStatus.SERVICE_UNAVAILABLE, data, headers, **kwargs)

    @classmethod
    def gateway_timeout(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 504 GATEWAY_TIMEOUT """
        return cls._make_response(HTTPStatus.GATEWAY_TIMEOUT, data, headers, **kwargs)

    @classmethod
    def http_version_not_supported(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 505 HTTP_VERSION_NOT_SUPPORTED """
        return cls._make_response(HTTPStatus.HTTP_VERSION_NOT_SUPPORTED, data, headers, **kwargs)

    @classmethod
    def variant_also_negotiates(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 506 VARIANT_ALSO_NEGOTIATES """
        return cls._make_response(HTTPStatus.VARIANT_ALSO_NEGOTIATES, data, headers, **kwargs)

    @classmethod
    def insufficient_storage(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 507 INSUFFICIENT_STORAGE """
        return cls._make_response(HTTPStatus.INSUFFICIENT_STORAGE, data, headers, **kwargs)

    @classmethod
    def loop_detected(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 508 LOOP_DETECTED """
        return cls._make_response(HTTPStatus.LOOP_DETECTED, data, headers, **kwargs)

    @classmethod
    def not_extended(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 510 NOT_EXTENDED """
        return cls._make_response(HTTPStatus.NOT_EXTENDED, data, headers, **kwargs)

    @classmethod
    def network_authentication_required(cls, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ HTTP 511 NETWORK_AUTHENTICATION_REQUIRED """
        return cls._make_response(HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED, data, headers, **kwargs)