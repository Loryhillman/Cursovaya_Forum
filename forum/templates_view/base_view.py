from abc import ABC, abstractmethod
from render_template import render_template

class View(ABC):
    template = ''
    headers = {}

    @abstractmethod
    def get(self, environ):
        pass

    def response(start_response):
        start_response("200 Ok", [("Content-type", "text/html")])