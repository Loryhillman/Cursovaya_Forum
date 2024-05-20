import cgi

from db.connect import send_message


class SendMessageView():
    def post(self, environ):
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        id_user_message = form.getvalue('id_user_message', '')
        message_text = form.getvalue('message_text', '')
        topic_id = form.getvalue('topic_id', '')
        send_message(id_user_message, message_text, topic_id)
        return b'{"status": "success"}', "application/json"
