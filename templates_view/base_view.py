from render_template import render_template
import mimetypes

class View:
    path = ''
    

    def response(self, environ, start_response):
        file_name = self.path + self.url
        mime_type, _ = mimetypes.guess_type(file_name)
        headers = [('Content-type', mime_type)]

        try:
            data = self.read_file(file_name[1:])
            status = '200 OK'
        except FileNotFoundError:
            data = ''
            status = '404 Not found'

        start_response(status, headers)
        return [data.encode('utf-8')]
    
    def read_file(self, file_name):
        print(file_name)
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()



