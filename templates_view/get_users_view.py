from db.connect import get_users_from_db

# Класс GetUsers, предназначенный для обработки запросов связанных с получением пользователей
class GetUsersView:
    
    def get(self, environ):
        return get_users_from_db()