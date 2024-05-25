import cgi

from db.connect import create_topic
from render_template import render_template
from templates_view.base_view import View

class CreateTopicView(View):
    template = 'templates/create_topic.html'
    def get(self, environ):
        """
        Обработка GET-запроса для отображения формы создания темы.

        Args:
        - `environ` (dict): Словарь с информацией о среде выполнения.

        Returns:
        - `str`: Строка с HTML-кодом формы создания темы.
        """
        return render_template(template_name=self.template, context={})
    def post(self, environ):
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        title = form.getvalue('title', '')
        author = form.getvalue('author', '')
        message = form.getvalue('message', '')
        date = form.getvalue('date', '')
        create_topic(title, author, message, date)
        return b'{"status": "success"}', "application/json"

