import cgi
from urllib.parse import parse_qs
from waitress import serve
from templates_view.index_view import IndexView
from templates_view.topics_view import TopicsView
from templates_view.topic_view import TopicView
from templates_view.profile_view import ProfileView
from templates_view.register_view import RegisterView
from templates_view.get_users_view import GetUsersView
from templates_view.get_topic_view import GetTopicView
from templates_view.new_topic_view import NewTopicView
from render_template import render_template
from templates_view.static_view import serve_static_file
from db.connect import send_message, get_messages_with_username, create_topic, create_user
import mimetypes

# Определение словаря для сопоставления URL-путей с классами представлений
routes = {
    "/" : IndexView,
    "/topics" : TopicsView,
    "/new_topic" : NewTopicView,
    "/topic": GetTopicView,
    "/users": GetUsersView,
    "/topic/": TopicView,
    "/profile": ProfileView,
    "/register": RegisterView
}

# Основная функция-обработчик запросов
def app(environ, start_response):
    # Извлечение пути из запроса
    path = environ.get("PATH_INFO")
    
    view_class = routes.get(path)
    view_instance = view_class()
    data = view_instance.response(environ, start_response)
    return iter([data])

    # # Обработка POST-запросов для отправки сообщений
    # if environ['REQUEST_METHOD'] == 'POST':
    #     if path == '/api/send_message':
    #         # Обработка POST-запроса для отправки сообщения
    #         form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    #         id_user_message = form.getvalue('id_user_message', '')
    #         message_text = form.getvalue('message_text', '')
    #         topic_id = form.getvalue('topic_id', '')
    #         send_message(id_user_message,message_text, topic_id)
    #         start_response("200 OK", [("Content-type", "application/json")])
    #         return [b'{"status": "success"}']
        
    # # Обработка POST-запроса для создания пользователя
    # if environ['REQUEST_METHOD'] == 'POST':
    #     if path == '/api/create_user':
    #         form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    #         login = form.getvalue('login', '')
    #         password_user = form.getvalue('password_user', '')
    #         create_user(login,password_user)
    #         start_response("200 OK", [("Content-type", "application/json")])
    #         return [b'{"status": "success"}']
    
    # # Обработка GET-запросов для получения сообщений с заданным идентификатором темы
    # if environ['REQUEST_METHOD'] == 'GET':
    #     if path == '/api/get_messages':
    #         query_string = environ.get('QUERY_STRING', '')
    #         query_params = parse_qs(query_string)
    #         topic_id = query_params.get('topic_id', [''])[0]
    #         response_data = get_messages_with_username(topic_id)
    #         if response_data:
    #             start_response("200 OK", [("Content-type", "application/json")])
    #             return [response_data.encode('utf-8')]
    #         else:
    #             start_response("500 Internal Server Error", [("Content-type", "application/json")])
    #             return [b'{"status": "error"}']
    
    # # Обработка POST-запросов для создания тем
    # if environ['REQUEST_METHOD'] == 'POST':
    #     if path == '/api/create_topic':
    #         form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    #         title = form.getvalue('title', '')
    #         author = form.getvalue('author', '')
    #         message = form.getvalue('message', '')
    #         date = form.getvalue('date', '')
    #         create_topic(title,author,message,date)
    #         start_response("200 OK", [("Content-type", "application/json")])
    #         return [b'{"status": "success"}']
        
    # # Проверка, связан ли путь с темой
    # if path.startswith("/topic/") and "/topic/" in routes:
    #     view_class = routes["/topic/"]
    # else:
    #     view_class = routes.get(path)
    
    # # Создание и вызов представления, обработка статических файлов
    # if view_class:
    #     view_instance = view_class()
    #     data = view_instance.get(environ)
    #     data = data.encode("utf-8")
    # else:
    #     response = serve_static_file(path, start_response)
    #     if response:
    #         return response
    #     data = render_template(template_name='templates/404.html', context={})
    #     data = data.encode("utf-8")

    # # Определение MIME-типа и установка заголовков ответа
    # mime_type, encoding = mimetypes.guess_type(path)
    # content_type = mime_type if mime_type else 'text/html'
    # if encoding:
    #     content_type += f'; charset={encoding}'
    # start_response("200 OK", [("Content-type", content_type)])
    # data = view_class.response(environ, start_response)
    # return iter([data])

if __name__ == "__main__":
    serve(app)
