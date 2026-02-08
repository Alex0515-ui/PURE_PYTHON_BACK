from enum import Enum

# Два вида роли
class Role(Enum):
    ADMIN = "admin"
    WORKER = "worker"

# Класс сущности User
class User:
    def __init__(self, id: int, name:str, role: Role, password: str | None = None):
        self.id = id
        self.name = name
        self.password = password
        self.role = role

        