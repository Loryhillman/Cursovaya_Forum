import mimetypes
"""
Args:
- `template_name` (str): Путь к файлу HTML-шаблона.
- `context` (dict, optional): Словарь с данными контекста для подстановки в шаблон. По умолчанию пустой словарь.

Returns:
- `str`: Сгенерированный HTML-код.
"""
def render_template(template_name, context={}):
    with open(template_name, 'r', encoding='utf-8') as f:
        html_str = f.read()
        html_str = html_str.format(*context)

    content_type, _ = mimetypes.guess_type(template_name)
    if content_type is None:
        content_type = 'text/html; charset=UTF-8'
    return html_str, content_type

