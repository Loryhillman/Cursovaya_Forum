from waitress import serve

from templates_view.index_view import IndexView
from templates_view.topic_view import TopicView
from templates_view.static_view import StaticView
from render_template import render_template
from templates_view.static_view import static_type
import mimetypes

adresses = {
    "/" : IndexView,
    "/topic" : TopicView,
    "/src/" : StaticView
}



def app(environ, start_response):
    path = environ.get("PATH_INFO")
   
    if path.startswith("/src/"):
        return static_type(path, start_response)


    if path in adresses:
        view_class = adresses[path]
        view_instance = view_class()
        data = view_instance.get(environ)
        content_type = 'text/html; charset=UTF-8'
        start_response(
        f"200 OK", [
            ("Content-type", content_type)

        ]
    )
    else:
        data = render_template(template_name="Forum/templates/404.html", context={})
        content_type = 'text/html; charset=UTF-8'
        start_response(
        f"200 OK", [
            ("Content-type", content_type)

        ]
    )
        

        
    data = data.encode("utf-8")
    



    return iter([data])

serve(app)