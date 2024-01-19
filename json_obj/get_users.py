from db.connect import get_users_from_db
class GetUsers:
    def get(self, environ):
        return get_users_from_db()