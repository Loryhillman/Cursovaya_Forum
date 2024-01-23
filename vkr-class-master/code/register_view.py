from templates_view.base_view import View
from render_template import render_template

class RegisterView(View):
    template = 'templates/register.html'
    def get(self, environ):
        """
        Обработка GET-запроса для страницы регистрации.

        Args:
        - `environ` (dict): Словарь с информацией о среде выполнения.

        Returns:
        - `str`: Строка с данными для ответа на GET-запрос.
        """
        return render_template(template_name=self.template, context={})
