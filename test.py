import sys
sys.path.insert(0, "app")

from app.tasks.repository import TaskRepository
from app.users.repository import UserRepository
from app.db.migrations import create_tables

# Создание таблицы
create_tables()
print("Таблицы созданы!")

# Создание пользователя
with UserRepository() as repo:
    user_id = repo.create_user("Alihan", "123")
    print(f"Пользователь с id: {user_id} успешно создан!")

    user = repo.get_user_by_name("Alihan")
    print(f"Пользователь получен: {dict(user)}")

# Создание задачи
with TaskRepository() as repo:
    task_id = repo.create_task("Task1", "Hello", "Alihan")
    print(f"Создана задача с id: {task_id}")

print("Все работает")
