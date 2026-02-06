# Валидатор для пользователя
class UserValidator:

    @staticmethod
    def validate(name, password, role):
        UserValidator.check_name(name)
        UserValidator.check_password(password)
        UserValidator.check_role(role)

    @staticmethod
    def check_name(name): # Проверка имени пользователя

        if not isinstance(name, str):
            raise ValueError("Имя должно быть строкой!")
        
        name = name.strip()
        if not name:
            raise ValueError("Заполните имя!")
        
        if len(name) < 3:
            raise ValueError("Имя должно включать не менее 3 символов!")
        
        return name
    
    @staticmethod
    def check_password(password): # Проверка пароля пользователя

        if not isinstance(password, str):
            raise ValueError("Введите пароль в виде строки!")
        
        password = password.strip()
        if not password:
            raise ValueError("Заполните пароль!")
        
        if len(password) < 3 or len(password) > 30:
            raise ValueError("Пароль должен быть длинной от 3 до 30 символов!")
        
        return password
    
    @staticmethod
    def check_role(role): # Проверка роли пользователя

        if role not in ["admin", "worker"]:
            raise ValueError("Нужно быть либо рабочим либо администратором!")
        
        return role
    
    
    

