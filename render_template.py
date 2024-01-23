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
    return html_str

