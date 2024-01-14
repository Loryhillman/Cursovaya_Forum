from waitress import serve
from templates_view.index_view import IndexView
from templates_view.topics_view import TopicsView
from templates_view.topic_page import TopicPage
from templates_view.user import UserView
from json_obj.get_users import GetUsers
from json_obj.get_topic import GetTopic
from templates_view.create_topic_view import Create_topicView
from render_template import render_template
from templates_view.static_view import serve_static_file
import mimetypes

adresses = {
    "/" : IndexView,
    "/topics" : TopicsView,
    "/create_topic" : Create_topicView,
    "/api/topic": GetTopic,
    "/api/users": GetUsers,
    "/topic/": TopicPage,
    "/profile": UserView
}

def app(environ, start_response):
    path = environ.get("PATH_INFO")
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

if __name__ == "__main__":
    serve(app)
