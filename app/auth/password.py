import hashlib

def hash_password(password:str):
    return hashlib.sha256(password.encode()).hexdigest() # <-- Хэширование пароля

def verify_password(password:str, hashed_password:str) -> bool:
    return hash_password(password) == hashed_password # <-- Проверка на совпадение паролей