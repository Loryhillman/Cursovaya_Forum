from db.connect import get_topics_from_db
from response import Response
from templates_view.base_view import View

class GetTopicView(View):
    def get(self, environ):
        """
        Обработка GET-запроса для получения списка тем.

        Args:
        - `environ` (dict): Словарь с информацией о среде выполнения.

        Returns:
        - `str`: Строка с данными для ответа на GET-запрос.
        """

    def get(self, environ):
        data = get_topics_from_db()
        content_type = "application/json"
        return Response(data=data, content_type=content_type, code=200)
