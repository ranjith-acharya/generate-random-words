import mysql.connector
import os

def connect_database():
    try:
        db = mysql.connector.connect(
            host = os.environ.get('DB_HOST'),
            user = os.environ.get('DB_USERNAME'),
            password = os.environ.get('DB_PASSWORD'),
            database = os.environ.get('DB_DATABASE')
        )
        cursor = db.cursor()
        return db, cursor

    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return None, None