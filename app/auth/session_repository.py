from app.db.connection import connection_to_db
import uuid
from datetime import datetime, timedelta

SESSION_EXPIRES = timedelta(hours=2)

# Класс для обращениям к сессий в БД
class SessionRepository:

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_to_db()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.connection:
            self.connection.close()

    # Создание сессии
    def create_session(self, user_id):
        session_id = str(uuid.uuid4()) #<-- Рандомная генерация ID
        now = datetime.now()
        expire = now + SESSION_EXPIRES
        cursor = self.connection.cursor()
        method = "INSERT INTO sessions (session_id, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)"
        cursor.execute(method, (session_id, user_id, now, expire))

        self.connection.commit()
        return session_id
    
    # Получение user_id из сессии
    def get_user_id(self, session_id):
        cursor = self.connection.cursor()
        method = "SELECT * FROM sessions WHERE session_id = ? AND expires_at > ?"
        cursor.execute(method, (session_id, datetime.now()))
        
        data = cursor.fetchone()
        return data["user_id"] if data else None
    
    # Удаление сессии
    def delete_session(self, session_id):
        cursor = self.connection.cursor()
        method = "DELETE FROM sessions WHERE session_id = ?"
        cursor.execute(method, (session_id, ))
        self.connection.commit()

    # Удаление сессии по истечении времени
    def expire_session(self):
        cursor = self.connection.cursor()
        method = "DELETE FROM sessions WHERE expires_at <= ?"
        cursor.execute(method, (datetime.now()))
        self.connection.commit()    