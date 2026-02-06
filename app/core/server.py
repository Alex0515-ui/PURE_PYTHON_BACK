from http.server import HTTPServer, BaseHTTPRequestHandler
from app.config import HOST, PORT
from app.core.routes import route
import json

# Базовый обработчик запросов
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()
    
    def do_PUT(self):
        self.handle_request()
    
    def do_DELETE(self):
        self.handle_request()

    def handle_request(self):
        try:
            result = route.resolve(self) 
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            if result:
                self.wfile.write(json.dumps(result).encode())
        
        except PermissionError as e:
            self.send_response(403)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(str(e).encode())

        except ValueError as e:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(str(e).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(str(e).encode())

# Функция для запуска сервера
def run():
    Server = HTTPServer((HOST, PORT), Handler) # <-- Сам сервер
    print(f"Сервер запущен на http://{HOST}:{PORT}")

    try:
        Server.serve_forever()
    except KeyboardInterrupt:
        print("Сервер остановлен") # <-- Остановка комбинацией Ctrl + C
    finally:
        Server.server_close()