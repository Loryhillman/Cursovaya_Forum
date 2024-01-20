import pymysql
import json
import base64
import pymysql.cursors
import requests

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


def send_message(id_user_message, message_text, topic_id):
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
                send_message_query = "INSERT INTO `messages` (`id_user_message`, `message_text`, `topic_id`) VALUES (%s, %s, %s)"
                cursor.execute(send_message_query, (id_user_message, message_text, topic_id))
                connection.commit()
                print("Message sended:", cursor.lastrowid)
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


def create_topic(title, author, message, date):
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
                create_topic_query = "INSERT INTO `topics` (`title`, `author`, `message`, `date`) VALUES (%s, %s, %s, %s)"
                cursor.execute(create_topic_query, (title, author, message, date))
                connection.commit()
                print("Topic created:", cursor.lastrowid)
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)

def create_user(login, password_user):
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
                create_user_query = "INSERT INTO `users` (`login`, `password`) VALUES (%s, %s)"
                cursor.execute(create_user_query, (login, password_user))
                connection.commit()
                print("User created:", cursor.lastrowid)
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


def get_messages_with_username(topic_id):
    messages = []
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Успешное подключение к базе данных")

        try:
            with connection.cursor() as cursor:
                select_all_rows = """
                    SELECT messages.id_message, messages.message_text, users.login
                    FROM `messages`
                    JOIN users ON messages.id_user_message = users.id_user
                    WHERE messages.topic_id = %s
                    ORDER BY messages.id_message ASC
                """
                cursor.execute(select_all_rows, (topic_id))
                rows = cursor.fetchall()
                for row in rows:
                    messages.append(row)
                json_string = json.dumps(messages)
                print(json_string)
                return json_string
        finally:
            connection.close()

    except Exception as ex:
        print("Отказано в соединении...")
        print(ex)



