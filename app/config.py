import os

# Создание порта и хоста сервера нашего
HOST = "0.0.0.0" # Для Docker необходим такой хост
PORT = 8000

# Создание путя к нашей базе данных
OUR_PROJ_PATH = os.path.dirname(os.path.abspath(__file__)) #Путь к нашему проекту
DB_PATH = os.path.join(OUR_PROJ_PATH, "myfirst.db")

# Отладка ошибок во время разработки
DEBUG = True









