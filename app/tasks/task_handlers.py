from app.tasks.task_service import TaskService
import json
from app.auth.session_handlers import get_user_session
from app.users.user_models import Role

task_service = TaskService()

# Создание задачи "/tasks/create"
def create_task(handler, params):
    admin = get_user_session(handler)

    if not admin:
        raise PermissionError("Нужно войти!")
    
    if admin.role != Role.ADMIN.value:
        raise PermissionError("Только админы могут создавать задачи!")
    
    length = int(handler.headers.get("Content-Length", 0)) # <-- Берет длину данных из заголовка
    body = handler.rfile.read(length) # <-- Читает тело запроса, точнее данные
    data = json.loads(body)

    task = task_service.create_task(
        title=data["title"], 
        description=data["description"], 
        assigned_to=data["assigned_to"]
    )
    
    return {
        "id": task.id,
        "title": task.title,
        "assigned_to": task.assigned_to
    }

# Получение задачи по ID "/tasks/id"
def get_task(handler, params):
    task_id = int(params["id"])
    task = task_service.get_task(task_id)

    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "assigned_to": task.assigned_to,
        "is_completed": task.is_completed
    }
    
# Получение всех задач пользователя "/users/tasks/id"
def get_tasks(handler, params):
    user = get_user_session(handler)
    user_id = int(params["id"])

    if not user:
        raise PermissionError("Нужно войти!")
    
    if user.role != Role.ADMIN.value and user.id != user_id:
        raise PermissionError("Только админы могут получать чужие задачи!")
    
    tasks = task_service.get_tasks(user_id)
    return tasks

# Завершение задачи "/tasks/id/complete"
def complete_task(handler, params):
    task_id = int(params["id"])
    user = get_user_session(handler)

    if not user:
        raise PermissionError("Нужно войти!")

    task_service.complete_task(user.id, task_id)
    task = task_service.get_task(task_id)

    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "assigned_to": task.assigned_to,
        "is_completed": task.is_completed
    }

# Удаление задачи "/tasks/id/delete"
def delete_task(handler, params):
    admin = get_user_session(handler)

    if not admin:
        raise PermissionError("Нужно войти!")
    
    if admin.role != Role.ADMIN.value:
        raise PermissionError("Только админы могут удалять задачи!")
    
    task_id = int(params["id"])
    task_service.delete_task(task_id)
    return {"message":"Task was successfully deleted!"}
