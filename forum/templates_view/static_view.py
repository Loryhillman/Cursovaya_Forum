from templates_view.base_view import View
import mimetypes


class StaticView(View):

    def get(self, environ):
        
        path = environ.get("PATH_INFO")
        new_path = path.replace('/', 'Forum/', 1)
        content_type, _ = mimetypes.guess_type(new_path)
        if not content_type:
            content_type = 'application/octet-stream'
        with open(new_path, 'rb') as file:
            data = file.read()
        headers = {"Content-type": content_type}
        return data, headers