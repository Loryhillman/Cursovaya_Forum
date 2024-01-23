from db.connect import get_topics_from_db
class GetTopicView:
    def get(self, environ):
        """
        Обработка GET-запроса для получения списка тем.

        Args:
        - `environ` (dict): Словарь с информацией о среде выполнения.

        Returns:
        - `str`: Строка с данными для ответа на GET-запрос.
        """
        return get_topics_from_db()