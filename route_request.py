import re
from routes import routes


def route_request(environ, start_response):
    path = environ.get("PATH_INFO")

    view_class = None
    for pattern, view in routes:
        if re.match(pattern, path):
            view_class = view
            break

    view_instance = view_class()
    response = view_instance.handle(environ)

    start_response(response.code, [("Content-type", response.content_type)])
    return [response.get_data()]


