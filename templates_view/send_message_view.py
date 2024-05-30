import cgi
from db.connect import send_message
from response import Response
from templates_view.base_view import View


class SendMessageView(View):
    def post(self, environ):
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        id_user_message = form.getvalue('id_user_message', '')
        message_text = form.getvalue('message_text', '')
        topic_id = form.getvalue('topic_id', '')
        send_message(id_user_message, message_text, topic_id)
        return Response(data='{"status": "success"}', content_type="application/json", code=200)
