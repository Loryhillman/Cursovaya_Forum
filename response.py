from codes import get_status_message


class Response:
    def __init__(self, data, content_type='text/html', code=200):
        self.data = data
        self.content_type = content_type
        self.status_code = code
        self.status_message = get_status_message(code)

    def get_data(self):
        return self.data.encode('utf-8') if isinstance(self.data, str) else self.data

    @property
    def code(self):
        return f"{self.status_code} {self.status_message}"