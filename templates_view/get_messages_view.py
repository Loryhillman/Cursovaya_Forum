from db.connect import get_messages_with_username
from urllib.parse import parse_qs
from templates_view.base_view import View
from response import Response

class GetMessagesView(View):
    def get(self, environ):
        """
        Обработка GET-запроса для получения списка тем.

        Args:
        - `environ` (dict): Словарь с информацией о среде выполнения.

        Returns:
        - `str`: Строка с данными для ответа на GET-запрос.
        """
        query_string = environ.get('QUERY_STRING', '')
        query_params = parse_qs(query_string)
        topic_id = query_params.get('topic_id', [''])[0]
        response_data = get_messages_with_username(topic_id)
        content_type = "application/json"
        return response_data, content_type

