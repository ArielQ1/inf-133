from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

estudiantes = [
    {
        "id": 1,
        "nombre": "Ariel",
        "apellido": "Quizaya",
        "carrera": "Informatica",
    },
    {
        "id": 2,
        "nombre": "Fabricio",
        "apellido": "Quispe",
        "carrera-mencion": "Seguridad de la Informacion",
    },
    {
        "id": 3,
        "nombre": "Ghilmar",
        "apellido": "Valeirano",
        "carrera-mencion": "Desarrollo de Software",
    },
    {
        "id": 4,
        "nombre": "Pica",
        "apellido": "Valencia",
        "carrera-mencion": "Inteligencia Artificial",
    },
    {
        "id": 5,
        "nombre": "Juan",
        "apellido": "Quispe",
        "carrera-mencion": "Desarrollo de Software",
    },
    {
        "id": 6,
        "nombre": "Pedrito",
        "apellido": "Guzman",
        "carrera-mencion": "TIC",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_DELETE(self):
        if self.path == '/estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        if parsed_path.path == "/estudiantes":
            if "nombre" in query_params:
                nombre = query_params["nombre"][0]
                estudiantes_filtrados = [
                    estudiante
                    for estudiante in estudiantes
                    if estudiante["nombre"] == nombre
                ]
                if estudiantes_filtrados != []:
                    self.response_handler(200, estudiantes_filtrados)
                else:
                    self.response_handler(204, [])
            else:
                self.response_handler(200,estudiantes)
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
      
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
    def do_POST(self):
        if self.path == '/estudiantes':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no Existente"}).encode('utf-8'))    

def run_server(port = 8000):
        try:
            server_address = ('', port)
            httpd = HTTPServer(server_address, RESTRequestHandler)
            print(f'Iniciando servidor web en http://localhost:{port}')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('Apagando Servidor web')
            httpd.socket.close()
                
if __name__ == "__main__":
    run_server()