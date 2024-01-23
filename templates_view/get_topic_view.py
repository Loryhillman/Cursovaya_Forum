from db.connect import get_topics_from_db

# Класс GetTopic, предназначенный для обработки запросов связанных с получением тем
class GetTopicView:
     # Метод get, который будет вызываться при обработке HTTP-запроса типа GET
    def get(self, environ):
        # Вызов функции get_topics_from_db для получения тем из базы данных
        return get_topics_from_db()