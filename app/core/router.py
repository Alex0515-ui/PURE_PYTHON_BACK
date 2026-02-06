import re

# Роутинг для создания URL строк с функциями
class Router:

    def __init__(self):
        self.routes = []

    def add(self, method, path, func):
        pattern = re.sub(r"{(\w+)}", r"(?P<\1>[^/]+)", path) # <-- Выражение позволяющее брать id из пути
        self.routes.append((method, re.compile(f"^{pattern}$"), func)) # <-- Комплириуем в объект рег. выражения

    # Вызов роута с функцией
    def resolve(self, handler):
        path = handler.path.split("?")[0] # <-- Убираем query параметры

        for method, regex, func in self.routes:
            match = regex.match(path)   

            if handler.command == method and match:
                params = match.groupdict() # /task/5 -> {"id": "5"}
                return func(handler, params)
