import cgi
from db.connect import create_topic
from templates_view.base_view import View
from response import Response
from templates_view.template_view import TemplateView


class CreateTopicView(TemplateView):

    template = 'templates/create_topic.html'

    def post(self, environ):
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        title = form.getvalue('title', '')
        author = form.getvalue('author', '')
        message = form.getvalue('message', '')
        date = form.getvalue('date', '')
        create_topic(title, author, message, date)
        return Response(data='{"status": "success"}', content_type="application/json", code=200)

