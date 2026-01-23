from ..db.connection import connection_to_db

# Класс функций для управления задачами в БД
class TaskRepository:

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_to_db()
        return self

    def __exit__(self, exc_type, exc_value, ext_tb):
        if self.connection:
            self.connection.close()
    
    # Создание задачи
    def create_task(self, title, description, assigned_to):
        cursor = self.connection.cursor()
        method = "INSERT INTO tasks (title, description, assigned_to) VALUES (?, ?, ?)"
        cursor.execute(method, (title, description, assigned_to))
        self.connection.commit()
        return cursor.lastrowid # Вернет по ID задачу
    
    # Удаление задачи
    def delete_task(self, id):
        cursor = self.connection.cursor()
        method = "DELETE FROM tasks WHERE id = ?"
        cursor.execute(method, (id, ))
        self.connection.commit()

    # Получение всех задач одного пользователя
    def get_tasks(self, user_id):
        cursor = self.connection.cursor()
        method = "SELECT * FROM tasks WHERE assigned_to = ?"
        cursor.execute(method, (user_id, ))
        return cursor.fetchall() # Вернет список задач