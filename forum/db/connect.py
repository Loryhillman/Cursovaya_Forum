import pymysql
import json
import base64
import pymysql.cursors

host = "localhost"
user = "root"
password = "mypassword"
db_name = "topic"

def get_topics_from_db():
    topics = []
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected")

        try: 
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `topics`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    topic = {
                        'title': row['title'],
                        'author': row['author'],
                        'date': row['date'],
                        'message': row['message']
                    }
                    topics.append(topic)
        finally:
            connection.close()
    except Exception as e:
        print(f"Failed to get topics from db: {e}")

    return topics