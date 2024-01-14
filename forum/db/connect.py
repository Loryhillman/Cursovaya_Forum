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
        print("Successfully connected to the database")

        try: 
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `topics`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    topics.append(row)
                json_string = json.dumps(topics)
                print(json_string)
                return json_string 
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)

def get_users_from_db():
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
        print("Successfully connected to the database")

        try: 
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `users`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    topics.append(row)
                json_string = json.dumps(topics)
                print(json_string)
                return json_string 
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)