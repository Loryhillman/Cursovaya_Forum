from waitress import serve
from webob import Response
from templates_view.index_view import IndexView
from templates_view.topic_view import TopicView
from templates_view.static_view import StaticView
from render_template import render_template

adresses = {
    "/" : IndexView,
    "/topic" : TopicView,
    "/src/" : StaticView
}

def app(environ, start_response):
    path = environ.get("PATH_INFO")
    response = Response()

    if path in adresses:
        view_class = adresses.get(path)
        view_instance = view_class()
        data, headers = view_instance.get(environ)
        response.body = data.encode("utf-8")
        response.headers.update(headers)
    elif path.startswith("/src/"):
        view_class = StaticView
        view_instance = view_class()
        data, headers = view_instance.get(environ)
        response.body = data
        response.headers.update(headers)
    else:
        data = render_template(template_name="Forum/templates/404.html", context={})
        response.body = data.encode("utf-8")
        response.headers["Content-type"] = 'text/html; charset=UTF-8'

    return response(environ, start_response)

serve(app)
