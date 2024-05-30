from templates_view.base_view import View
from render_template import render_template
from response import Response

class ErrorView(View):
    template = 'templates/404.html'
    def get(self, environ):
        """
        Обработка GET-запроса для главной страницы.

        Args:
        - `environ` (dict): Словарь с информацией о среде выполнения.

        Returns:
        - `str`: Строка с данными для ответа на GET-запрос.
        """
        # Рендеринг шаблона и возврат данных и заголовков
        data = render_template(template_name=self.template, context={})

        return Response(data=data, content_type='text/html', code=404)