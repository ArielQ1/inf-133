from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
chocolates = {}


class Chocolate:
    def __init__(self, chocolate_type, peso, sabor, relleno):
        self.chocolate_type = chocolate_type
        self.peso = peso
        self.sabor = sabor
        self.relleno = relleno
        
class Tabletas(Chocolate):
    def __init__(self, peso, sabor, relleno = None):
        super().__init__("tableta", peso, sabor, relleno)


class Bombones(Chocolate):
    def __init__(self, peso, sabor, relleno):
        super().__init__("bombon", peso, sabor, relleno)
class Trufas(Chocolate):
    def __init__(self, peso, sabor, relleno):
        super().__init__("trufa", peso, sabor, relleno)
class ChocolateFactory:
    @staticmethod
    def create_chocolate(chocolate_type, peso, sabor, relleno):
        if chocolate_type == "tableta":
            return Tabletas(peso, sabor)
        elif chocolate_type == "bombon":
            return Bombones(peso, sabor, relleno)
        elif chocolate_type == "trufa":
            return Trufas(peso, sabor, relleno)
        else:
            raise ValueError("Tipo de Chocolate de entrega no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class ChocolateService:
    def __init__(self):
        self.factory = ChocolateFactory()

    def add_chocolate(self, data):
        chocolate_type = data.get("chocolate_type", None)
        peso = data.get("peso", None)
        sabor = data.get("sabor", None)
        relleno = data.get("relleno", None)

        factory_chocolate = self.factory.create_chocolate(
            chocolate_type, peso, sabor, relleno
        )        
        
        chocolates[len(chocolates) + 1] = factory_chocolate
        

    def list_chocolates(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()}

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id not in chocolates:
            return None
        
        chocolate = chocolates[chocolate_id]
        chocolate.peso = data.get("peso", chocolate.peso)
        chocolate.sabor = data.get("sabor", chocolate.sabor)        
        chocolate.relleno = data.get("relleno", chocolate.relleno)
        
        return chocolate

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in chocolates:
            del chocolates[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:
            return None


class ChocolateRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.chocolate_service = ChocolateService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.chocolate_service.list_chocolates()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.update_chocolate(chocolate_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.chocolate_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, ChocolateRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()