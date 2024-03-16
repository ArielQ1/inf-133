from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema, Field

class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()
    
estudiantes = [
    Estudiante(id=1, nombre="Ariel", apellido="Quizaya", carrera="Ingeniería de Sistemas"),
    Estudiante(id=2, nombre="Pedrito", apellido="Lopez", carrera="Arquitectura"),
    Estudiante(id=3, nombre="Ariel", apellido="Callisaya", carrera="Diseno Grafico"),
    Estudiante(id=4, nombre="Pedrito", apellido="Quispe", carrera="Arquitectura"),
    Estudiante(id=5, nombre="Ariel", apellido="Yujra", carrera="Medicina"),
    Estudiante(id=6, nombre="Pedrito", apellido="Mamani", carrera="Enfermeria"),
]

class Query(ObjectType):
    estudiantes = List(Estudiante)
    estudiantes1 = List(Estudiante, carrera=String())
    estudiante = Field(Estudiante, id=Int())
    estudiante1 = Field(Estudiante, nombre=String(), apellido=String())
    estu = Field(Estudiante, carrera=String(), nombre= String())
    
    def resolve_estudiantes1(root, info, carrera):
        listita = []
        for estudiante in estudiantes:
            print(estudiante)
            if estudiante.carrera == carrera:
                listita.append(estudiante)
        if not listita:
            return None
        else:
            return listita
    
    def resolve_estudiante1(root, info, nombre, apellido):
        for estudiante in estudiantes:
            if estudiante.nombre == nombre and estudiante.apellido == apellido:
                return estudiante
        return None
    
    def resolve_estu(root, info, carrera, nombre):
        for estudiante in estudiantes:
            if estudiante.carrera == carrera and estudiante.nombre == nombre:
                return estudiante
        return None

    def resolve_estudiantes(root, info):
        return estudiantes

    def resolve_estudiante(root, info, id):
        for estudiante in estudiantes:
            if estudiante.id == id: 
                return estudiante
        return None
    
schema = Schema(query=Query)
    
class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
        
    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})
            
def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run_server()