import sys

sys.path.append("../")
import config
from send_request import send_request


def test_http_version_incorrect() -> str:
    request_header = 'GET / HTTP/0.1\r\nHost:{}\r\n\r\n'.format(
        config.SERVER_NAME)
    http_response = send_request(request_header)
    if http_response.status != 505 and http_response.status // 100 != 4:
        return "Bad status code: {}, expected: {}".format(str(http_response.status), '505 or 4XX')
    return ""
