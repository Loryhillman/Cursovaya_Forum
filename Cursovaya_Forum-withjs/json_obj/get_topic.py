from db.connect import get_topics_from_db
class GetTopic:
    def get(self, environ):
        return get_topics_from_db()