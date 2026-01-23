# HTTP сервер
from http.server import HTTPServer, BaseHTTPRequestHandler

# Функция обработчика ответов
class MyHandler(BaseHTTPRequestHandler):
    def do_get(self):
        self.send_response(200)
        path = self.path

        response = f"<h1>404: Page {path} not found</h1>".encode('utf-8')
        if path == "/login":
            response = b"<h1>Profile page</h1>"
        elif path == "/Tasks":
            response = b"<h1>"
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write("HELLO".encode('utf-8'))

# Создание порта и название сервера
hostname = "localhost"
server_port = 8000

# Создание самого сервера
web_server = HTTPServer((hostname, server_port), MyHandler)
print(f"Сервер запущен: http://{hostname}:{server_port}")

# Работа самого сервера
try:
    web_server.serve_forever()
except KeyboardInterrupt: # Прекращение при нажатии Ctrl + C
    print("Работа сервера прервана клавишами")

web_server.server_close()
print("Сервер остановлен...")