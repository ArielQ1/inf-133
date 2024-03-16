import requests

# Definir la consulta GraphQL
query = '''
    {
        estudiantes1(carrera: "Arquitectura"){
            id
        }
    }
'''

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)