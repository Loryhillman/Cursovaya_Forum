import cgi

from db.connect import create_user
from templates_view.base_view import View

class CreateUserView(View):
    def post(self, environ):
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        login = form.getvalue('login', '')
        password_user = form.getvalue('password_user', '')
        create_user(login, password_user)
        return b'{"status": "success"}', "application/json"

