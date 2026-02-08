# Класс сущности Task
class Task:
    def __init__(self, id: int, title: str, description: str, is_completed: bool, assigned_to: int):
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = is_completed
        self.assigned_to = assigned_to


        