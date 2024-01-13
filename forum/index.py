from waitress import serve
from templates_view.index_view import IndexView
from templates_view.topics_view import TopicsView
from templates_view.create_topic_view import Create_topicView
from templates_view.static_view import StaticView
from render_template import render_template

adresses = {
    "/" : IndexView,
    "/topics" : TopicsView,
    "/create_topic" : Create_topicView
}

def set_status_and_response(start_response, data, headers, status="200 OK"):
    start_response(status, [(key, value) for key, value in headers.items()])
    if isinstance(data, str):
        data = data.encode("utf-8")
    return iter([data])

def app(environ, start_response):
    path = environ.get("PATH_INFO")

    if path in adresses:
        view_class = adresses.get(path)
        view_instance = view_class()
        data, headers = view_instance.get(environ)
        return set_status_and_response(start_response, data, headers)
    elif path.startswith("/src/"):
        view_class = StaticView
        view_instance = view_class()
        data, headers = view_instance.get(environ)
        return set_status_and_response(start_response, data, headers)
    else:
        data = render_template(template_name="templates/404.html", context={})
        headers = {"Content-type": 'text/html; charset=UTF-8'}
        return set_status_and_response(start_response, data, headers, status="404 Not Found")

serve(app)