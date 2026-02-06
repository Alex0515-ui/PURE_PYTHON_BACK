from app.auth.session_repository import SessionRepository
from app.users.user_repository import UserRepository
from app.auth.password import verify_password

# Класс бизнес логики сессии
class SessionService:

    # Логика логина
    def login(self, name, password):
        with SessionRepository() as session, UserRepository() as users:
            user = users.get_user_by_name(name)

            if not user:
                raise ValueError("Такого пользователя не существует!")
            
            if not verify_password(password, user["password"]):
                raise ValueError("Неверный пароль!")
            
            return session.create_session(user["id"])
    
    # Логика выхода
    def logout(self, session_id):
        with SessionRepository() as session:
            session.delete_session(session_id)

