from templates_view.base_view import View
from render_template import render_template

class TopicView(View):
    template = 'Forum/templates/topic.html'
    headers = {"Content-type": 'text/html; charset=UTF-8'}
    
    def get(self, environ):
        return render_template(template_name=self.template, context={}), self.headers
