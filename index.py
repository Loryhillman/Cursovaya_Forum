from waitress import serve
from route_request import route_request

def app(environ, start_response):
    return iter(route_request(environ, start_response))

if __name__ == "__main__":
    serve(app)