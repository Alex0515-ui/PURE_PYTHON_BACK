from ..db.connection import connection_to_db

# Класс функций для обращения к БД
class UserRepository:
    
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_to_db()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.connection:
            self.connection.close()

    # Функция для создания пользователя в БД
    def create_user(self, name, password, role: str = "worker"):
        cursor = self.connection.cursor()
        method = "INSERT INTO users (name, password, role) VALUES (?, ?, ?)"
        cursor.execute(method, (name, password, role))
        self.connection.commit()
        return cursor.lastrowid # Возвращает ID пользователя нашего
    
    # Функция для получения пользователя по имени в БД
    def get_user_by_name(self, name):
        cursor = self.connection.cursor()
        method = "SELECT * FROM users WHERE name = ?"
        cursor.execute(method, (name, ))
        return cursor.fetchone() # Вернет объект как словарь