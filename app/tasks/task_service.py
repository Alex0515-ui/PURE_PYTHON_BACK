from app.tasks.task_models import Task
from app.tasks.task_validator import TaskValidator
from app.tasks.task_repository import TaskRepository
from app.users.user_repository import UserRepository

# Класс функций для управления задачами
class TaskService:

    # Создание задачи
    def create_task(self, title, description, assigned_to):
        TaskValidator.validate(title, description)
        task = Task(id=None, 
                    title = title,
                    description=description, 
                    is_completed=False, 
                    assigned_to=assigned_to)
        
        with UserRepository() as repo:
            user_id = repo.get_user_by_id(assigned_to)
            if not user_id:
                raise ValueError("Пользователь с таким ID не найден!")
        
        repo = TaskRepository()
        with repo:
            task_id = repo.create_task(task.title, task.description, task.assigned_to)
            task.id = task_id

        return task
    
    # Завершение задачи
    def complete_task(self, user_id, task_id):
        with TaskRepository() as repo:
            task = repo.get_task(task_id)

            if not task:
                raise ValueError("Нет задачи с таким ID")
            
            if task.assigned_to != user_id:
                raise ValueError("Эта задача не для тебя!")
            
            if task.is_completed:
                raise ValueError("Задача уже завершена!")
            
            repo.complete_task(task_id)

    # Получение всех задач пользователя
    def get_tasks(self, user_id):
        with TaskRepository() as repo:
            tasks = repo.get_user_tasks(user_id)
        return tasks 
    
    # Получение задачи по ID
    def get_task(self, task_id):
        with TaskRepository() as repo:
            task = repo.get_task(task_id)

            if not task:
                raise ValueError("Такой задачи нету!")
        return task
    
    
    # Удаление задачи по ID
    def delete_task(self, task_id):
        with TaskRepository() as repo:
            task = repo.get_task(task_id)
            
            if not task:
                raise ValueError("Такой задачи нету!")
            repo.delete_task(task_id)

            
                