# Валидатор для задачи
class TaskValidator:

    @staticmethod
    def validate(title, description): # Метод объединяющий два прошлых метода для чистого кода в сервисе
        TaskValidator.check_title(title)
        TaskValidator.check_description(description)

    @staticmethod
    def check_title(title): # Проверка названия задачи

        if not isinstance(title, str):
            raise ValueError("Название должно быть строкой!")
        
        title = title.strip()
        if not title:
            raise ValueError("Нужно дать название для задания!")
        
        if len(title) < 3 or len(title) > 100:
            raise ValueError("Длина названия задания должна быть от 3 до 100 символов!")
        
        return title
        
    @staticmethod
    def check_description(description): # Проверка описания задачи
        
        if not isinstance(description, str):
            raise ValueError("Описание должно быть в виде строки!")
        
        description = description.strip()
        if not description:
            raise ValueError("Дайте описание для задачи!")
        
        if len(description) > 5000:
            raise ValueError("Описание должно быть не больше 5000 символов!")
        
        return description
        

    
        