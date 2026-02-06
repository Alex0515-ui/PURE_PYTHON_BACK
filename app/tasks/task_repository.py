from app.db.connection import connection_to_db
from app.tasks.task_models import Task

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
        return cursor.lastrowid # Вернет задачу по ID
    
    # Получение одной задачи по ID
    def get_task(self, task_id):
        cursor = self.connection.cursor()
        method = "SELECT * FROM tasks WHERE id = ?"
        cursor.execute(method, (task_id, ))
        task = cursor.fetchone() # Один объект Row
        if not task:
            return None

        return Task(
            id= task["id"], 
            title=task["title"], 
            description=task["description"], 
            is_completed=task["is_completed"],
            assigned_to=task["assigned_to"]
            )
    
    # Получение всех задач одного пользователя
    def get_user_tasks(self, user_id):
        cursor = self.connection.cursor()
        method = "SELECT * FROM tasks WHERE assigned_to = ?"
        cursor.execute(method, (user_id, ))
        tasks = cursor.fetchall() # Вернет список задач
        return [{k: task[k] for k in task.keys()} for task in tasks]
    
    # Удаление задачи
    def delete_task(self, id):
        cursor = self.connection.cursor()
        method = "DELETE FROM tasks WHERE id = ?"
        cursor.execute(method, (id, ))
        self.connection.commit()

    # Завершение задачи
    def complete_task(self, task_id):
        cursor = self.connection.cursor()
        method = "UPDATE tasks SET is_completed = 1 WHERE id = ?"
        cursor.execute(method, (task_id, ))
        self.connection.commit()