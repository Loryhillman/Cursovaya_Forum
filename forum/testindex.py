from waitress import serve

def render_template(template_name='index.html', context={}):

    html_str=""
    with open(template_name, 'r') as f:
        html_str=f.read()
        html_str=html_str.format(**context)
    return html_str

def home(environ):
    return render_template(template_name='index.html', context={})

def contact_us(environ):
    return render_template(template_name='contact.html', context={})

def contact2(environ):
    return render_template(template_name='2.html', context={})

def app(environ, start_response):
    path= environ.get("PATH_INFO")
    if path == "/":
        data = home(environ)
    elif path == "/contact":
        data = contact_us(environ)
    elif path == "/contact/2":
        data = contact2(environ)
    else:
        data = render_template(template_name='404.html', context={"path":path})
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-type", "text/html"),
            ("Content-Lenght", str(len("abc")))
        ]
    )
    return iter([data])

serve(app)