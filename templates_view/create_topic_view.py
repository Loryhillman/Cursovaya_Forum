from templates_view.base_view import View
import cgi
from db.connect import create_topic

class CreateTopicView(View):

    def create_topic(self, environ):
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        title = form.getvalue('title', '')
        author = form.getvalue('author', '')
        message = form.getvalue('message', '')
        date = form.getvalue('date', '')
        create_topic(title,author,message,date)
        start_response("200 OK", [("Content-type", "application/json")])
        return [b'{"status": "success"}']
