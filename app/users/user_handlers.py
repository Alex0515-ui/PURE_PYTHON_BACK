from app.users.user_service import UserService
import json
from app.auth.session_handlers import get_user_session
from app.users.user_models import Role

user_service = UserService()

# Создание пользователя (регистрация) "/users/create"
def create_user(handler, params):
    length = int(handler.headers.get("Content-Length", 0)) # <-- Берет длину байтов данных
    body = handler.rfile.read(length) # <-- Читает данные из body запроса
    user_data = json.loads(body)

    user = user_service.create_user(name=user_data["name"], 
                             password=user_data["password"], 
                             role=user_data["role"])    
    return {
        "name": user.name,
        "role": user.role
    }

# Получение пользователя "/users/id"
def get_user(handler, params):
    user_id = int(params["id"])
    user = user_service.get_user(user_id)

    return {
        "id": user.id,
        "name": user.name,
        "role": user.role
    }

# Удаление пользователя "/users/id/delete"
def delete_user(handler, params):
    admin = get_user_session(handler)

    if not admin:
        raise PermissionError("Нужно войти в систему!")
    
    if admin.role != Role.ADMIN.value:
        raise PermissionError("Только администраторы могут удалять пользователей!")
    
    user_id = int(params["id"])
    
    user_service.delete_user(user_id, admin.id)

# Изменение роли "/users/id/role"
def update_user_role(handler, params):
    admin = get_user_session(handler)

    if not admin:
        raise PermissionError("Нужно войти в систему!")
    
    if admin.role != Role.ADMIN.value:
        raise PermissionError("Только администраторы могут менять роль пользователям!")
    
    user_id = int(params["id"])

    length = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(length)
    data = json.loads(body)

    role = data.get("role")

    user_service.update_user_role(admin.id, user_id, role)