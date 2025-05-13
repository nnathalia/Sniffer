from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class LoginHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")  # permite CORS
        self.end_headers()

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            data = parse_qs(post_data)
            user = data.get("user", [""])[0]
            password = data.get("password", [""])[0]

            print(f"Login recebido: usuário='{user}', senha='{password}'")

            # Resposta de sucesso ou erro simples
            if user == "admin" and password == "123":
                self._set_headers(200)
                self.wfile.write(b'{"status": "ok"}')
            else:
                self._set_headers(401)
                self.wfile.write(b'{"status": "erro"}')
        else:
            self._set_headers(404)
            self.wfile.write(b'{"status": "not found"}')

def run(server_class=HTTPServer, handler_class=LoginHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando em http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
