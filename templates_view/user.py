from templates_view.template_view import TemplateView

"""""
Properties:
- `template` (str): Путь к файлу HTML-шаблона для отображения страницы.

Methods:
- `get(self, environ) -> str`: Метод для обработки GET-запросов и возвращения HTML-кода страницы.

Attributes:
- `template` (str): Путь к файлу HTML-шаблона для отображения страницы.
"""


class UserView(TemplateView):
    template = 'templates/user.html'
