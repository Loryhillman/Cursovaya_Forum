from waitress import serve
from routes import route_request

def app(environ, start_response):
    return iter(route_request(environ, start_response))

if __name__ == "__main__":
    serve(app)