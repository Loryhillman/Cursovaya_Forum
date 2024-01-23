import pymysql
import json
import base64
import pymysql.cursors
import requests

host = "localhost"
user = "root"
password = "mypassword"
db_name = "topic"

def create_connection():
    try:
        return pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

    except Exception as ex:
        print("Connection refused...")
        print(ex)
        return None

def execute_query(connection, query, parameters=None, commit=False):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, parameters)
            result = cursor.fetchall()
            if commit:
                connection.commit()
            return result

    except Exception as ex:
        print(f"Error executing query: {ex}")
        return None

def get_data_from_db(query, parameters=None):
    connection = create_connection()

    if connection:
        try:
            result = execute_query(connection, query, parameters)
            json_string = json.dumps(result)
            print(json_string)
            return json_string

        finally:
            connection.close()

def get_topics_from_db():
    query = "SELECT * FROM `topics`"
    return get_data_from_db(query)

def get_users_from_db():
    query = "SELECT * FROM `users`"
    return get_data_from_db(query)

def send_message(id_user_message, message_text, topic_id):
    query = "INSERT INTO `messages` (`id_user_message`, `message_text`, `topic_id`) VALUES (%s, %s, %s)"
    parameters = (id_user_message, message_text, topic_id)
    execute_query(create_connection(), query, parameters, commit=True)
    print("Message sent successfully.")

def create_topic(title, author, message, date):
    query = "INSERT INTO `topics` (`title`, `author`, `message`, `date`) VALUES (%s, %s, %s, %s)"
    parameters = (title, author, message, date)
    execute_query(create_connection(), query, parameters, commit=True)
    print("Topic created successfully.")

def create_user(login, password_user):
    query = "INSERT INTO `users` (`login`, `password`) VALUES (%s, %s)"
    parameters = (login, password_user)
    execute_query(create_connection(), query, parameters, commit=True)
    print("User created successfully.")

def get_messages_with_username(topic_id):
    query = """
        SELECT messages.id_message, messages.message_text, users.login
        FROM `messages`
        JOIN users ON messages.id_user_message = users.id_user
        WHERE messages.topic_id = %s
        ORDER BY messages.id_message ASC
    """
    parameters = (topic_id,)
    return get_data_from_db(query, parameters)