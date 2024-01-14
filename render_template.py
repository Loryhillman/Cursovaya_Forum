def render_template(template_name, context={}):
    with open(template_name, 'r', encoding='utf-8') as f:
        html_str = f.read()
        html_str = html_str.format(*context)
    return html_str
