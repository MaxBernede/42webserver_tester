import sys

sys.path.append("../")
from send_request import send_request
import config

def test_auth_no_key() -> str:
    request_header = "GET /protected HTTP/1.1\r\nHost:{}\r\n\r\n".format(
        config.SERVER_NAME
    )
    http_response = send_request(request_header)
    if http_response.status != 401:
        return "Bad status code: {}, expected: {}".format(
            str(http_response.status), "401"
        )
    if http_response.headers["WWW-Authenticate"] == None:
        return "Missing 'WWW-Authenticate' header"
    return ""


def test_auth() -> str:
    request_header = (
        "GET /protected HTTP/1.1\r\nHost:{}\r\nAuthorization: {}\r\n\r\n".format(
            config.SERVER_NAME, config.AUTH_KEY
        )
    )
    http_response = send_request(request_header)
    if http_response.status != 200:
        return "Bad status code: {}, expected: {}".format(
            str(http_response.status), "200"
        )
    return ""
