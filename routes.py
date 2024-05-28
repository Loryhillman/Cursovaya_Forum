import re
from render_template import render_template
from templates_view.create_user_view import CreateUserView
from templates_view.send_message_view import SendMessageView
from templates_view.index_view import IndexView
from templates_view.topics_view import TopicsView
from templates_view.topic_page_view import TopicPageView
from templates_view.user import UserView
from templates_view.register_view import RegisterView
from templates_view.get_users_view import GetUsersView
from templates_view.get_topic_view import GetTopicView
from templates_view.get_messages_view import GetMessagesView
from templates_view.create_topic_view import CreateTopicView
from templates_view.static_view import StaticView
from templates_view.error_view import ErrorView

routes = [
    (r'^/$', IndexView),
    (r'/topics$', TopicsView),
    (r'/topic$', GetTopicView),
    (r'/users$', GetUsersView),
    (r'/topic/.*$', TopicPageView),
    (r'/profile$', UserView),
    (r'/register$', RegisterView),
    (r'/api/send_message$', SendMessageView),
    (r'/create_user$', CreateUserView),
    (r'/create_topic$', CreateTopicView),
    (r'/api/create_topic$', CreateTopicView),
    (r'/api/get_messages$', GetMessagesView),
    (r'^/src/.*$', StaticView),
    (r'.*', ErrorView)
]

def route_request(environ, start_response):
    path = environ.get("PATH_INFO")

    view_class = None
    for pattern, view in routes:
        if re.match(pattern, path):
            view_class = view
            break

    view_instance = view_class()
    data, content_type = view_instance.handle(environ)

    data = data.encode("utf-8") if isinstance(data, str) else data
    start_response("200 OK", [("Content-type", content_type)])
    return [data]