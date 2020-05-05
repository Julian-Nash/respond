from typing import Optional, Union

from flask import make_response, jsonify, Response
from httpz import HTTPStatusCodeEnum as HTTPStatusCode


class JSONResponse(object):
    """ Class for returning JSON responses """

    @classmethod
    def _send_response(
        cls,
        status_code: int,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = None,
        headers: Optional[dict] = None,
    ) -> Response:
        """ Builds and returns a flask Response """
        resp: Response = make_response(jsonify(data or ""), status_code)
        if headers:
            resp.headers.update(**headers)
        return resp

    @classmethod
    def continue_(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 100 Continue

        This interim response indicates that everything so far is OK and that the client should continue the request,
        or ignore the response if the request is already finished
        """
        return cls._send_response(HTTPStatusCode.CONTINUE.value, data, headers)

    @classmethod
    def switching_protocol(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 101 Switching Protocol

        This code is sent in response to an Upgrade request header from the client, and indicates the protocol the
        server is switching to
        """
        return cls._send_response(
            HTTPStatusCode.SWITCHING_PROTOCOL.value, data, headers
        )

    @classmethod
    def processing(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 102 Processing

        This code indicates that the server has received and is processing the request, but no response is available yet
        """
        return cls._send_response(HTTPStatusCode.PROCESSING.value, data, headers)

    @classmethod
    def early_hints(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 103 Early Hints

        This status code is primarily intended to be used with the Link header, letting the user agent start preloading
        resources while the server prepares a response
        """
        return cls._send_response(HTTPStatusCode.EARLY_HINTS.value, data, headers)

    @classmethod
    def ok(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 200 OK

        The request has succeeded
        """
        return cls._send_response(HTTPStatusCode.OK.value, data, headers)

    @classmethod
    def created(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 201 Created

        The request has succeeded and a new resource has been created as a result
        """
        return cls._send_response(HTTPStatusCode.CREATED.value, data, headers)

    @classmethod
    def accepted(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 202 Accepted

        The request has been received but not yet acted upon
        """
        return cls._send_response(HTTPStatusCode.ACCEPTED.value, data, headers)

    @classmethod
    def non_authoritative_information(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 203 Non-Authoritative Information

        The returned meta-information is not exactly the same as is available from the origin server, but is collected
        from a local or a third-party copy
        """
        return cls._send_response(
            HTTPStatusCode.NON_AUTHORITATIVE_INFORMATION.value, data, headers
        )

    @classmethod
    def no_content(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 204 No Content

        There is no content to send for this request, but the headers may be useful. The user-agent may update its
        cached headers for this resource with the new ones
        """
        return cls._send_response(HTTPStatusCode.NO_CONTENT.value, data, headers)

    @classmethod
    def reset_content(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 205 Reset Content

        Tells the user-agent to reset the document which sent this request
        """
        return cls._send_response(HTTPStatusCode.RESET_CONTENT.value, data, headers)

    @classmethod
    def partial_content(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 206 Partial Content

        This response code is used when the Range header is sent from the client to request only part of a resource
        """
        return cls._send_response(HTTPStatusCode.PARTIAL_CONTENT.value, data, headers)

    @classmethod
    def multi_status(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 207 Multi-Status

        Conveys information about multiple resources, for situations where multiple status codes might be appropriate
        """
        return cls._send_response(HTTPStatusCode.MULTI_STATUS.value, data, headers)

    @classmethod
    def already_reported(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 208 Already Reported

        Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple
        bindings to the same collection
        """
        return cls._send_response(HTTPStatusCode.ALREADY_REPORTED.value, data, headers)

    @classmethod
    def im_used(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 226 IM Used

        The server has fulfilled a GET request for the resource, and the response is a representation of the result of
        one or more instance-manipulations applied to the current instance
        """
        return cls._send_response(HTTPStatusCode.IM_USED.value, data, headers)

    @classmethod
    def multiple_choice(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 300 Multiple Choice

        The request has more than one possible response. The user-agent or user should choose one of them
        """
        return cls._send_response(HTTPStatusCode.MULTIPLE_CHOICE.value, data, headers)

    @classmethod
    def moved_permanently(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 301 Moved Permanently

        The URL of the requested resource has been changed permanently. The new URL is given in the response
        """
        return cls._send_response(HTTPStatusCode.MOVED_PERMANENTLY.value, data, headers)

    @classmethod
    def found(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 302 Found

        This response code means that the URI of requested resource has been changed temporarily. Further changes in
        the URI might be made in the future
        """
        return cls._send_response(HTTPStatusCode.FOUND.value, data, headers)

    @classmethod
    def see_other(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 303 See Other

        The server sent this response to direct the client to get the requested resource at another URI with a GET
        request
        """
        return cls._send_response(HTTPStatusCode.SEE_OTHER.value, data, headers)

    @classmethod
    def not_modified(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 304 Not Modified

        This is used for caching purposes. It tells the client that the response has not been modified, so the client
        can continue to use the same cached version of the response
        """
        return cls._send_response(HTTPStatusCode.NOT_MODIFIED.value, data, headers)

    @classmethod
    def use_proxy(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 305 Use Proxy

        Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed
        by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy
        """
        return cls._send_response(HTTPStatusCode.USE_PROXY.value, data, headers)

    @classmethod
    def unused(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 306 Unused

        This response code is no longer used; it is just reserved. It was used in a previous version of the HTTP/1.1
        specification
        """
        return cls._send_response(HTTPStatusCode.UNUSED.value, data, headers)

    @classmethod
    def temporary_redirect(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 307 Temporary Redirect

        The server sends this response to direct the client to get the requested resource at another URI with same
        method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code,
        with the exception that the user agent must not change the HTTP method used
        """
        return cls._send_response(
            HTTPStatusCode.TEMPORARY_REDIRECT.value, data, headers
        )

    @classmethod
    def permanent_redirect(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 308 Permanent Redirect

        This means that the resource is now permanently located at another URI, specified by the Location: HTTP
        Response header. This has the same semantics as the 301 Moved Permanently HTTP response code, with the
        exception that the user agent must not change the HTTP method used
        """
        return cls._send_response(
            HTTPStatusCode.PERMANENT_REDIRECT.value, data, headers
        )

    @classmethod
    def bad_request(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 400 Bad Request

        The server could not understand the request due to invalid syntax
        """
        return cls._send_response(HTTPStatusCode.BAD_REQUEST.value, data, headers)

    @classmethod
    def unauthorized(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 401 Unauthorized

        Although the HTTP standard specifies 'unauthorized', semantically this response means 'unauthenticated'. That
        is, the client must authenticate itself to get the requested response
        """
        return cls._send_response(HTTPStatusCode.UNAUTHORIZED.value, data, headers)

    @classmethod
    def payment_required(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 402 Payment Required

        Although the HTTP standard specifies 'unauthorized', semantically this response means 'unauthenticated'. That
        is, the client must authenticate itself to get the requested response
        """
        return cls._send_response(HTTPStatusCode.PAYMENT_REQUIRED.value, data, headers)

    @classmethod
    def forbidden(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 403 Forbidden

        The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing
        to give the requested resource. Unlike 401, the client's identity is known to the server
        """
        return cls._send_response(HTTPStatusCode.FORBIDDEN.value, data, headers)

    @classmethod
    def not_found(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 404 Not Found

        The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API,
        this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send
        this response instead of 403 to hide the existence of a resource from an unauthorized client
        """
        return cls._send_response(HTTPStatusCode.NOT_FOUND.value, data, headers)

    @classmethod
    def method_not_allowed(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 405 Method Not Allowed

        The request method is known by the server but has been disabled and cannot be used. For example, an API may
        forbid DELETE-ing a resource. The two mandatory methods, GET and HEAD, must never be disabled and should not
        return this error code
        """
        return cls._send_response(
            HTTPStatusCode.METHOD_NOT_ALLOWED.value, data, headers
        )

    @classmethod
    def not_acceptable(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 406 Not Acceptable

        This response is sent when the web server, after performing server-driven content negotiation, doesn't find any
        content that conforms to the criteria given by the user agent
        """
        return cls._send_response(HTTPStatusCode.NOT_ACCEPTABLE.value, data, headers)

    @classmethod
    def proxy_authentication_required(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 407 Proxy Authentication Required

        This is similar to 401 but authentication is needed to be done by a proxy
        """
        return cls._send_response(
            HTTPStatusCode.PROXY_AUTHENTICATION_REQUIRED.value, data, headers
        )

    @classmethod
    def request_timeout(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 408 Request Timeout

        This response is sent on an idle connection by some servers, even without any previous request by the client.
        It means that the server would like to shut down this unused connection
        """
        return cls._send_response(HTTPStatusCode.REQUEST_TIMEOUT.value, data, headers)

    @classmethod
    def conflict(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 409 Conflict

        This response is sent when a request conflicts with the current state of the server
        """
        return cls._send_response(HTTPStatusCode.CONFLICT.value, data, headers)

    @classmethod
    def gone(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 410 Gone

        This response is sent when the requested content has been permanently deleted from server, with no forwarding
        address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends
        this status code to be used for 'limited-time, promotional services'. APIs should not feel compelled to
        indicate resources that have been deleted with this status code
        """
        return cls._send_response(HTTPStatusCode.GONE.value, data, headers)

    @classmethod
    def length_required(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 411 Length Required

        Server rejected the request because the Content-Length header field is not defined and the server requires it
        """
        return cls._send_response(HTTPStatusCode.LENGTH_REQUIRED.value, data, headers)

    @classmethod
    def precondition_failed(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 412 Precondition Failed

        The client has indicated preconditions in its headers which the server does not meet
        """
        return cls._send_response(
            HTTPStatusCode.PRECONDITION_FAILED.value, data, headers
        )

    @classmethod
    def payload_too_large(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 413 Payload Too Large

        Request entity is larger than limits defined by server; the server might close the connection or return an
        Retry-After header field
        """
        return cls._send_response(HTTPStatusCode.PAYLOAD_TOO_LARGE.value, data, headers)

    @classmethod
    def uri_too_long(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 414 URI Too Long

        The URI requested by the client is longer than the server is willing to interpret
        """
        return cls._send_response(HTTPStatusCode.URI_TOO_LONG.value, data, headers)

    @classmethod
    def unsupported_media_type(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 415 Unsupported Media Type

        The media format of the requested data is not supported by the server, so the server is rejecting the request
        """
        return cls._send_response(
            HTTPStatusCode.UNSUPPORTED_MEDIA_TYPE.value, data, headers
        )

    @classmethod
    def requested_range_not_satisfiable(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 416 Range Not Satisfiable

        The range specified by the Range header field in the request can't be fulfilled; it's possible that the range
        is outside the size of the target URI's data
        """
        return cls._send_response(
            HTTPStatusCode.REQUESTED_RANGE_NOT_SATISFIABLE.value, data, headers
        )

    @classmethod
    def expectation_failed(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 417 Expectation Failed

        This response code means the expectation indicated by the Expect request header field can't be met by the server
        """
        return cls._send_response(
            HTTPStatusCode.EXPECTATION_FAILED.value, data, headers
        )

    @classmethod
    def im_a_teapot(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 418 I'm a teapot

        The server refuses the attempt to brew coffee with a teapot
        """
        return cls._send_response(HTTPStatusCode.IM_A_TEAPOT.value, data, headers)

    @classmethod
    def misdirected_request(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 421 Misdirected Request

        The request was directed at a server that is not able to produce a response. This can be sent by a server that
        is not configured to produce responses for the combination of scheme and authority that are included in the
        request URI
        """
        return cls._send_response(
            HTTPStatusCode.MISDIRECTED_REQUEST.value, data, headers
        )

    @classmethod
    def unprocessable_entity(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 422 Unprocessable Entity

        The request was well-formed but was unable to be followed due to semantic errors
        """
        return cls._send_response(
            HTTPStatusCode.UNPROCESSABLE_ENTITY.value, data, headers
        )

    @classmethod
    def locked(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 423 Locked

        The resource that is being accessed is locked
        """
        return cls._send_response(HTTPStatusCode.LOCKED.value, data, headers)

    @classmethod
    def failed_dependency(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 424 Failed Dependency

        The request failed due to failure of a previous request
        """
        return cls._send_response(HTTPStatusCode.FAILED_DEPENDENCY.value, data, headers)

    @classmethod
    def too_early(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 425 Too Early

        Indicates that the server is unwilling to risk processing a request that might be replayed
        """
        return cls._send_response(HTTPStatusCode.TOO_EARLY.value, data, headers)

    @classmethod
    def upgrade_required(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 426 Upgrade Required

        The server refuses to perform the request using the current protocol but might be willing to do so after the
        client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the
        required protocol(s)
        """
        return cls._send_response(HTTPStatusCode.UPGRADE_REQUIRED.value, data, headers)

    @classmethod
    def precondition_required(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 428 Precondition Required

        The origin server requires the request to be conditional. This response is intended to prevent the 'lost update'
        problem, where a client GETs a resource's state, modifies it, and PUTs it back to the server, when meanwhile
        a third party has modified the state on the server, leading to a conflict
        """
        return cls._send_response(
            HTTPStatusCode.PRECONDITION_REQUIRED.value, data, headers
        )

    @classmethod
    def too_many_requests(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 429 Too Many Requests

        The user has sent too many requests in a given amount of time
        """
        return cls._send_response(HTTPStatusCode.TOO_MANY_REQUESTS.value, data, headers)

    @classmethod
    def request_header_fields_too_large(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 431 Request Header Fields Too Large

        The server is unwilling to process the request because its header fields are too large. The request may be
        resubmitted after reducing the size of the request header fields
        """
        return cls._send_response(
            HTTPStatusCode.REQUEST_HEADER_FIELDS_TOO_LARGE.value, data, headers
        )

    @classmethod
    def unavailable_for_legal_reasons(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 451 Unavailable For Legal Reasons

        The server is unwilling to process the request because its header fields are too large. The request may be
        resubmitted after reducing the size of the request header fields
        """
        return cls._send_response(
            HTTPStatusCode.UNAVAILABLE_FOR_LEGAL_REASONS.value, data, headers
        )

    @classmethod
    def internal_server_error(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 500 Internal Server Error

        The server has encountered a situation it doesn't know how to handle
        """
        return cls._send_response(
            HTTPStatusCode.INTERNAL_SERVER_ERROR.value, data, headers
        )

    @classmethod
    def not_implemented(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 501 Not Implemented

        The request method is not supported by the server and cannot be handled. The only methods that servers are
        required to support (and therefore that must not return this code) are GET and HEAD
        """
        return cls._send_response(HTTPStatusCode.NOT_IMPLEMENTED.value, data, headers)

    @classmethod
    def bad_gateway(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 502 Bad Gateway

        This error response means that the server, while working as a gateway to get a response needed to handle the
        request, got an invalid response
        """
        return cls._send_response(HTTPStatusCode.BAD_GATEWAY.value, data, headers)

    @classmethod
    def service_unavailable(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 503 Service Unavailable

        The server is not ready to handle the request. Common causes are a server that is down for maintenance or that
        is overloaded. Note that together with this response, a user-friendly page explaining the problem should be
        sent. This responses should be used for temporary conditions and the Retry-After: HTTP header should, if
        possible, contain the estimated time before the recovery of the service. The webmaster must also take care
        about the caching-related headers that are sent along with this response, as these temporary condition
        responses should usually not be cached
        """
        return cls._send_response(
            HTTPStatusCode.SERVICE_UNAVAILABLE.value, data, headers
        )

    @classmethod
    def gateway_timeout(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 504 Gateway Timeout

        This error response is given when the server is acting as a gateway and cannot get a response in time
        """
        return cls._send_response(HTTPStatusCode.GATEWAY_TIMEOUT.value, data, headers)

    @classmethod
    def http_version_not_supported(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 505 HTTP Version Not Supported

        The HTTP version used in the request is not supported by the server
        """
        return cls._send_response(
            HTTPStatusCode.HTTP_VERSION_NOT_SUPPORTED.value, data, headers
        )

    @classmethod
    def variant_also_negotiates(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 506 Variant Also Negotiates

        The server has an internal configuration error: the chosen variant resource is configured to engage in
        transparent content negotiation itself, and is therefore not a proper end point in the negotiation process
        """
        return cls._send_response(
            HTTPStatusCode.VARIANT_ALSO_NEGOTIATES.value, data, headers
        )

    @classmethod
    def insufficient_storage(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 507 Insufficient Storage

        The method could not be performed on the resource because the server is unable to store the representation
        needed to successfully complete the request
        """
        return cls._send_response(
            HTTPStatusCode.INSUFFICIENT_STORAGE.value, data, headers
        )

    @classmethod
    def loop_detected(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 508 Loop Detected

        The server detected an infinite loop while processing the request
        """
        return cls._send_response(HTTPStatusCode.LOOP_DETECTED.value, data, headers)

    @classmethod
    def not_extended(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 510 Not Extended

        Further extensions to the request are required for the server to fulfil it
        """
        return cls._send_response(HTTPStatusCode.NOT_EXTENDED.value, data, headers)

    @classmethod
    def network_authentication_required(
        cls,
        data: Optional[Union[str, int, float, bool, list, dict, None]] = "",
        headers: Optional[dict] = None,
    ) -> Response:
        """ HTTP 511 Network Authentication Required

        The 511 status code indicates that the client needs to authenticate to gain network access
        """
        return cls._send_response(
            HTTPStatusCode.NETWORK_AUTHENTICATION_REQUIRED.value, data, headers
        )
