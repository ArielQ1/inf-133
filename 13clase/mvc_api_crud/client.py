import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo libro
url = f"{BASE_URL}/books"
nuevo_libro = {"title": "Juan", "author": "Felino", "edition": "primera", "availability": "siempre"}
response = requests.post(url, json=nuevo_libro, headers=headers)
print("Creando un nuevo libro:")
print(response.json())

# Crear el segundo libro
libro_2 = {"title": "Jhin", "author": "Juan", "edition": "segunda", "availability": "poca"}
response = requests.post(url, json=libro_2, headers=headers)
print("\nCreando el segundo libro:")
print(response.json())

# Obtener la lista de todos los libros
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print("\nLista de Libros:")
print(response.json())

# Obtener un libro específico por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/books/1"
response = requests.get(url, headers=headers)
print("\nDetalles del libro con ID 1:")
print(response.json())

# Actualizar un animal existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/books/2"
datos_actualizacion = {"title": "act", "author": "act", "edition": "act", "availability": "act"}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el libro con ID 1:")
print(response.json())

# Eliminar un animal existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/books/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el libro con ID 1:")
if response.status_code == 204:
    print(f"Libro con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")
