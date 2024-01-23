import pymysql
import json

# Параметры подключения к базе данных
host = "localhost"
user = "root"
password = "mypassword"
db_name = "topic"

def get_connection():
    return pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(query, *args):
    try:
        connection = get_connection()
        print("Successfully connected to the database")
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            rows = cursor.fetchall()
            result = [row for row in rows]
            json_string = json.dumps(result)
            return json_string
    except Exception as ex:
        print("Connection refused...")
        print(ex)
    finally:
        connection.close()

def send_query(query, *args):
    try:
        connection = get_connection()
        print("Successfully connected to the database")
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            connection.commit()
            print("Operation successful:", cursor.lastrowid)
    except Exception as ex:
        print("Connection refused...")
        print(ex)
    finally:
        connection.close()

def get_topics_from_db():
    query = "SELECT * FROM `topics`"
    return execute_query(query)

def get_users_from_db():
    query = "SELECT * FROM `users`"
    return execute_query(query)

def send_message(id_user_message, message_text, topic_id):
    query = "INSERT INTO `messages` (`id_user_message`, `message_text`, `topic_id`) VALUES (%s, %s, %s)"
    send_query(query, id_user_message, message_text, topic_id)

def create_topic(title, author, message, date):
    query = "INSERT INTO `topics` (`title`, `author`, `message`, `date`) VALUES (%s, %s, %s, %s)"
    send_query(query, title, author, message, date)

def create_user(login, password_user):
    query = "INSERT INTO `users` (`login`, `password`) VALUES (%s, %s)"
    send_query(query, login, password_user)

def get_messages_with_username(topic_id):
    query = """
        SELECT messages.id_message, messages.message_text, users.login
        FROM `messages`
        JOIN users ON messages.id_user_message = users.id_user
        WHERE messages.topic_id = %s
        ORDER BY messages.id_message ASC
    """
    return execute_query(query, topic_id)