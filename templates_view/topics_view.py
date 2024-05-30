from response import Response
from templates_view.base_view import View
from render_template import render_template

"""
Properties:
- `template` (str): Путь к файлу HTML-шаблона для отображения страницы.

Methods:
- `get(self, environ) -> str`: Метод для обработки GET-запросов и возвращения HTML-кода страницы.

Attributes:
- `template` (str): Путь к файлу HTML-шаблона для отображения страницы.
"""
class TopicsView(View):
    template = 'templates/topics.html'
    def get(self, environ):
        """
    Метод для обработки GET-запросов и возвращения HTML-кода страницы.

    Args:
    - `environ` (dict): Словарь с данными окружения запроса WSGI.

    Returns:
    - `str`: Сгенерированный HTML-код страницы.
        """
        data = render_template(template_name=self.template, context={})

        return Response(data=data, content_type='text/html', code=200)
