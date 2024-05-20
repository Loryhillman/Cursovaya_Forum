from db.connect import get_users_from_db
class GetUsersView:
    def get(self, environ):
        """
        Обработка GET-запроса для получения списка пользователей.

        Args:
        - `environ` (dict): Словарь с информацией о среде выполнения.

        Returns:
        - `str`: Строка с данными для ответа на GET-запрос.
        """

        data = get_users_from_db()
        content_type = "application/json"
        return data, content_type