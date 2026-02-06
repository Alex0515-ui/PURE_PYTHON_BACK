from app.db.connection import connection_to_db
from app.users.user_models import User

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
    
    # Функция для получения пользователя по ID в БД
    def get_user_by_id(self, user_id):
        cursor = self.connection.cursor()
        method = "SELECT * FROM users WHERE id = ?"
        cursor.execute(method, (user_id, ))
        user = cursor.fetchone() # Объект как словарь

        if not user:
            return None
        
        return User(
            id=user["id"], 
            name=user["name"], 
            role=user["role"]
        )
    
    # Удаление пользователя по ID в БД
    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        method = "DELETE FROM users WHERE id = ?"
        cursor.execute(method, (user_id, ))
        self.connection.commit()

    # Получение пользователя по имени для логина и тд
    def get_user_by_name(self, name):
        cursor = self.connection.cursor()
        method = "SELECT * FROM users WHERE name = ?"
        cursor.execute(method, (name, ))
        return cursor.fetchone() # Вернет объект как словарь
    
    # Проверка существует ли пользователь
    def user_exists(self, user_id):
        cursor = self.connection.cursor()
        method = "SELECT 1 FROM users WHERE id = ?"
        cursor.execute(method, (user_id, ))
        return cursor.fetchone() is not None # Вернет True/False
    
    # Обновление роли пользователя
    def update_role(self, user_id, new_role):
        cursor = self.connection.cursor()
        method = "UPDATE users SET role = ? WHERE id = ?"
        cursor.execute(method, (new_role, user_id) )
        self.connection.commit()
