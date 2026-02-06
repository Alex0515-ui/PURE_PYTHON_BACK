from app.db.connection import connection_to_db

# Функция для создания таблиц БД
def create_tables():

    connection = connection_to_db() 
    cursor = connection.cursor() # Установка курсора для создания таблиц в БД

    # Таблица пользователя
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
                   )
    ''')

    # Таблица задачи
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        is_completed BOOLEAN DEFAULT 0,     
        assigned_to INTEGER NOT NULL,
        FOREIGN KEY (assigned_to) REFERENCES users (id)
        )
''')
    # Таблица сессий
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        session_id TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL,
        created_at TIMESTAMP NOT NULL,
        expires_at TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)         
    )
''')
    
    connection.commit() # Сохраняем все
    connection.close()
    print("Таблицы в базе данных успешно созданы!")

if __name__ == "__main__":
    create_tables()





