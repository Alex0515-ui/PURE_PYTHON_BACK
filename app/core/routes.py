from app.core.router import Router
from app.tasks.task_handlers import create_task, complete_task, delete_task, get_task, get_tasks
from app.users.user_handlers import create_user, get_user, delete_user, update_user_role
from app.auth.session_handlers import login

route = Router()

# Пути для tasks
route.add("POST", "/tasks/create", create_task)
route.add("PUT", r"^/tasks/(?P<id>\d+)/complete$", complete_task)
route.add("DELETE", r"^/tasks/(?P<id>\d+)/delete$", delete_task)
route.add("GET", r"^/users/tasks/(?P<id>\d+)$", get_tasks)
route.add("GET", r"^/tasks/(?P<id>\d+)$", get_task)

# Пути для users
route.add("POST", "/users/create", create_user)
route.add("GET", r"^/users/(?P<id>\d+)$", get_user)
route.add("DELETE", r"^/users/(?P<id>\d+)/delete$", delete_user)
route.add("PUT", r"^/users/(?P<id>\d+)/role$", update_user_role)

# Путь для login
route.add("POST", "/login", login)

