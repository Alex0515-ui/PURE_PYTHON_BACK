from ..users.model import Role
from models import Task

# Класс функций для управления задачами
class TaskService:

    def __init__(self, tasks, users, role:Role):
        self.tasks = tasks
        self.users = users
        self.role = role

    # Создание задачи
    def create_task(self, title, description, is_completed, assigned_to):
        if self.role != Role.ADMIN:
            raise PermissionError("Только администраторы могут создавать задачи!")
        
        task = Task(id=None, 
                    title = title,
                    description=description, 
                    is_completed=is_completed, 
                    assigned_to=assigned_to)
        
        self.tasks.add(task)
        return task
    
    # Завершение задачи
    def complete_task(self, worker, task_id):
        task = self.tasks.get(task_id)

        if task.assigned_to != worker.name:
            raise PermissionError("Эта задача не для тебя!")
        
        task.is_completed = True
        self.tasks.delete(task_id)