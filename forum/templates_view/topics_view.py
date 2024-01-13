from templates_view.base_view import View
from render_template import render_template
from db.connect import get_topics_from_db

class TopicsView(View):
    template = 'templates/topics.html'
    headers = {"Content-type": 'text/html; charset=UTF-8'}
    
    def get(self, environ):
        # Получаем топики из базы данных
        topics = get_topics_from_db()

        # Формируем HTML-код динамически
        topic_html = ""
        for topic in topics:
            topic_html += """
                <section class="topic-content">
                    <h1>{}</h1>
                    <div class="topic-details">
                        <p>Автор: {}</p>
                        <p>Дата: {}</p>
                    </div>
                    <div class="topic-body">
                        <p>{}</p>
                    </div>
                </section>
            """.format(topic['title'], topic['author'], topic['date'], topic['message'])

        # Заменяем метку в вашем HTML на динамически сформированный код
        with open(self.template, 'r', encoding='utf-8') as template_file:
            html_str = template_file.read()
        
        html_content = html_str.replace('{% content %}', topic_html)

        return html_content, self.headers