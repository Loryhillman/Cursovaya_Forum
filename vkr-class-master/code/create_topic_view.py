from templates_view.base_view import View
from render_template import render_template

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
