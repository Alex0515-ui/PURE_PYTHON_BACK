import os

# Создание порта и хоста сервера нашего
HOST = "localhost"
PORT = 8000

# Создание путя к нашей базе данных
OUR_PROJ_PATH = os.path.dirname(os.path.abspath(__file__)) #Путь к нашему проекту
DB_PATH = os.path.join(OUR_PROJ_PATH, "myfirst.db")

# Отладка ошибок во время разработки
DEBUG = True

# Создание версии API, если вдруг версия поменяется
API_VERSION = "v1"
API_PATH = f"/api/{API_VERSION}"








