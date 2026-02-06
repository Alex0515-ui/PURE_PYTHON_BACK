import json
from app.auth.session_service import SessionService
from http.cookies import SimpleCookie
from app.users.user_repository import UserRepository
from app.auth.session_repository import SessionRepository

session_service = SessionService()

# Логин с созданием cookie
def login(handler, params):
    length = int(handler.headers.get("Content-Length", 0))
    body = handler.rfile.read(length)
    data = json.loads(body)

    session_id = session_service.login(data["name"], data["password"])

    handler.send_response(200)
    handler.send_header('Set-cookie', f"session_id={session_id}; HttpOnly; MaxAge=7200")
    handler.end_headers()

    handler.wfile.write(b"{'message': 'You logged succesfully!'}")

# Получить ID сессии из cookie
def get_session_id(handler):
    data = handler.headers.get("Cookie")

    if not data:
        return None
    
    cookie = SimpleCookie()
    cookie.load(data)
    if "session_id" not in cookie:
        return None
    
    return cookie["session_id"].value

# Получение пользователя через сессии
def get_user_session(handler):
    session_id = get_session_id(handler)

    if not session_id:
        return None
    
    with UserRepository() as users, SessionRepository() as session:
        user_id = session.get_user_id(session_id)

        if not user_id:
            return None
        
        return users.get_user_by_id(user_id)
        
# Выход с удалением сессии и cookie
def logout(handler):
    session_id = get_session_id(handler)

    if session_id:
        session_service.logout(session_id)

    handler.send_response(200)
    handler.send_header("Set-Cookie", "session_id=; Max-Age=0; HttpOnly")
    handler.end_headers()


    
    