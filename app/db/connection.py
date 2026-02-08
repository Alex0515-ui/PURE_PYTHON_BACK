import sqlite3
from app.config import DB_PATH

# Функция для создания подключения к нашей БД
def connection_to_db():
    connection = sqlite3.connect(database=DB_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row # Позволяет нам обращаться к колонкам по именам

    return connection