from db.connect import get_topics_from_db
from response import Response
from templates_view.base_view import View

class GetTopicView(View):

    def get(self, environ):
        data = get_topics_from_db()
        content_type = "application/json"
        return Response(data=data, content_type=content_type, code=200)
