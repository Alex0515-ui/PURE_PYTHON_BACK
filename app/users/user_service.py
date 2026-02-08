from app.users.user_validator import UserValidator
from app.users.user_models import User, Role
from app.users.user_repository import UserRepository
from app.auth.password import hash_password

# Класс функций для работы с пользователем
class UserService:

    # Создание пользователя
    def create_user(self, name, password, role):
        hashed_password = hash_password(password)
        UserValidator.validate(name, password, role)
        
        with UserRepository() as repo:
            if repo.get_user_by_name(name):
                raise ValueError("Пользователь уже существует!")
            user_id = repo.create_user(name, hashed_password, role)

        return User(
            id=user_id,
            name=name, 
            password=hashed_password,
            role=role
        )

    # Получения пользователя
    def get_user(self, user_id):
        with UserRepository() as repo:
            user = repo.get_user_by_id(user_id)

            if not user:
                raise ValueError("Такого пользователя не существует!")
    
        return user
    
    # Удаление пользователя по ID
    def delete_user(self, user_id, admin_id):
        with UserRepository() as repo:
            admin = repo.get_user_by_id(admin_id)
            if not admin:
                raise ValueError("Такого администратора нету!")
            
            if admin["role"] != Role.ADMIN.value:
                raise PermissionError("Только администраторы могут удалять пользователей!")
            
            if not repo.user_exists(user_id):
                raise ValueError("Такого пользователя не существует!")

            repo.delete_user(user_id)
        return {"message": "Пользователь был успешно удален!"}
    
    # Обновление роли
    def update_user_role(self, admin_id, user_id, role):
        with UserRepository() as repo:
            admin = repo.get_user_by_id(admin_id)

            if not admin:
                raise ValueError("Такого админа не существует!")
            
            if admin.role != Role.ADMIN.value:
                raise PermissionError("Только администраторы могут менять роли пользователей!")
            
            if not repo.user_exists(user_id):
                raise ValueError("Такого пользователя не существует!")
            
            UserValidator.check_role(role)
            repo.update_role(user_id, role)

        