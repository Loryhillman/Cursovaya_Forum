from urllib.parse import parse_qs
import cgi
from render_template import render_template
from templates_view.static_view import serve_static_file
from db.connect import send_message, get_messages_with_username, create_topic, create_user
import mimetypes
from templates_view.index_view import IndexView
from templates_view.topics_view import TopicsView
from templates_view.topic_page_view import TopicPageView
from templates_view.user import UserView
from templates_view.register_view import RegisterView
from templates_view.get_users_view import GetUsersView
from templates_view.get_topic_view import GetTopicView
from templates_view.create_topic_view import CreateTopicView

adresses = {
    "/" : IndexView,
    "/topics" : TopicsView,
    "/create_topic" : CreateTopicView,
    "/topic": GetTopicView,
    "/users": GetUsersView,
    "/topic/": TopicPageView,
    "/profile": UserView,
    "/register": RegisterView
}

def route_request(environ, start_response):
    path = environ.get("PATH_INFO")

    if environ['REQUEST_METHOD'] == 'POST':
        if path == '/api/send_message':
            form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
            id_user_message = form.getvalue('id_user_message', '')
            message_text = form.getvalue('message_text', '')
            topic_id = form.getvalue('topic_id', '')
            send_message(id_user_message, message_text, topic_id)
            start_response("200 OK", [("Content-type", "application/json")])
            return [b'{"status": "success"}']

        if path == '/api/create_user':
            form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
            login = form.getvalue('login', '')
            password_user = form.getvalue('password_user', '')
            create_user(login, password_user)
            start_response("200 OK", [("Content-type", "application/json")])
            return [b'{"status": "success"}']

        if path == '/api/create_topic':
            form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
            title = form.getvalue('title', '')
            author = form.getvalue('author', '')
            message = form.getvalue('message', '')
            date = form.getvalue('date', '')
            create_topic(title, author, message, date)
            start_response("200 OK", [("Content-type", "application/json")])
            return [b'{"status": "success"}']

    if environ['REQUEST_METHOD'] == 'GET':
        if path == '/api/get_messages':
            query_string = environ.get('QUERY_STRING', '')
            query_params = parse_qs(query_string)
            topic_id = query_params.get('topic_id', [''])[0]
            response_data = get_messages_with_username(topic_id)
            if response_data:
                start_response("200 OK", [("Content-type", "application/json")])
                return [response_data.encode('utf-8')]
            else:
                start_response("500 Internal Server Error", [("Content-type", "application/json")])
                return [b'{"status": "error"}']

    if path.startswith("/topic/") and "/topic/" in adresses:
        view_class = adresses["/topic/"]
    else:
        view_class = adresses.get(path)
    if view_class:
        view_instance = view_class()
        data = view_instance.get(environ)
        data = data.encode("utf-8")
    else:
        response = serve_static_file(path, start_response)
        if response:
            return response
        data = render_template(template_name='templates/404.html', context={})
        data = data.encode("utf-8")

    mime_type, encoding = mimetypes.guess_type(path)
    content_type = mime_type if mime_type else 'text/html'
    if encoding:
        content_type += f'; charset={encoding}'
    start_response("200 OK", [("Content-type", content_type)])
    return iter([data])