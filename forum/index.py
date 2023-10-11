from waitress import serve
import sys
from pprint import pprint
    
def render_template(template_name='index.html', context={}):

    html_str=""
    with open(template_name, "r") as f:
        html_str=f.read()
        html_str=html_str.format(**context)
    
    return html_str

def mainpage(environ):
    return render_template(template_name='P:\Projects_from_python\Kursovaya_Forum\Forum\index.html', context={})

def topic(environ):
    return render_template(template_name='topic.html', context={})

def app(environ, start_response):
    path = environ.get("PATH_INFO")
    if path == "/":
        data = mainpage(environ)
    else:
        data = render_template(template_name='404.html', context={"path":path})
    data = data.encode("utf-8")
    
    start_response(
        f"200 OK", [
            ("Content-type", "text/html")
        ]
    )

    return iter([data])
print(sys.path)
serve(app)