from waitress import serve

from templates_view.index_view import IndexView
from templates_view.topic_view import TopicView
from render_template import render_template
from serve_file import serve_file
import mimetypes

adresses = {
    "/" : IndexView,
    "/topic" : TopicView,
}



def app(environ, start_response):
    path = environ.get("PATH_INFO")

    if path.startswith("/src/"):
        return serve_file(path, start_response)

    if path in adresses:
        view_class = adresses[path]
        view_instance = view_class()
        data = view_instance.get(environ)
        content_type = 'text/html; charset=UTF-8'
    else:
        data = render_template(template_name="Forum/templates/404.html", context={})
        content_type = 'text/html; charset=UTF-8'
        
    data = data.encode("utf-8")
    
    start_response(
        f"200 OK", [
            ("Content-type", content_type)

        ]
    )



    return iter([data])

serve(app)