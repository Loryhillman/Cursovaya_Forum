from templates_view.base_view import View
from render_template import render_template

class IndexView(View):
    template = 'templates/index.html'
    def get(self, environ):
        # Рендеринг шаблона и возврат данных и заголовков
        return render_template(template_name=self.template, context={})
