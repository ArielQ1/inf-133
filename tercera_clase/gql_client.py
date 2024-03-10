import requests

#Definir la consulta GraphQL
query = """
    {
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
        
    }
"""
url = 'http://localhost:8000/graphql'

response = requests.post(url, json={'query':query})
print(response.text)