from render_template import render_template

class View():
    template = ''

    def get(self, environ):
        pass

    def post(self, environ):
        pass

    def handle(self, environ):

        request_method = environ['REQUEST_METHOD']

        if request_method == 'GET':
            return self.get(environ)
        else:
            return self.post(environ)

