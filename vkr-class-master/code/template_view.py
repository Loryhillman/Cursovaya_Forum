from response import Response
from templates_view.base_view import View
from render_template import render_template


class TemplateView(View):

    template = ''

    def get(self, environ):
        data = render_template(template_name=self.template, context={})
        return Response(data=data, content_type='text/html', code=200)