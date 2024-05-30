status_messages = {
    200: 'OK',
    404: 'Not Found',
    201: 'Created',
    500: 'Internal Server Error'
}


def get_status_message(code):
    return status_messages.get(code, 'Unknown Status')