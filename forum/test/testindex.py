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
    return render_template(template_name='templates\index.html', context={})

def topic(environ):
    return render_template(template_name='templates\\topic.html', context={})

adresses = {
    "/" : mainpage,
    "/topic" : topic,
}

def adress_parse(path, environ):
    data = adresses[path]
    return data(environ)




def app(environ, start_response):
    path = environ.get("PATH_INFO")


    if path in adresses:
        data = adress_parse(path, environ)
    else:
        data = render_template(template_name='templates\\404.html', context={"path":path})
        
    data = data.encode("utf-8")
    
    start_response(
        f"200 OK", [
            ("Content-type", "text/html; charset=utf-8")

        ]
    )



    return iter([data])
print(sys.path)
serve(app)