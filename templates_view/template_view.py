from templates_view.base_view import View
import mimetypes
from render_template import render_template

class TemplateView(View):
    template = ""

    def response(self, environ, start_response):
        path = environ.get("PATH_INFO")
        mime_type, _ = mimetypes.guess_type(path)
        headers = [('Content-type', mime_type)]
        try:
            data = render_template(path)
            status = '200 OK'
        except FileNotFoundError:
            data = ''
            status = '404 Not found'
        start_response(status, headers)
        return [data.encode('utf-8')]
    
