import mimetypes
from templates_view.base_view import View

class StaticView(View):
    def get(self, environ):
        path = environ.get('PATH_INFO', '')
        new_path = path.lstrip('/')
        try:
            with open(new_path, 'rb') as f:
                content = f.read()
            mime_type, _ = mimetypes.guess_type(new_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'
            return content, mime_type
        except FileNotFoundError:
            return b"404 Not Found", "text/plain"