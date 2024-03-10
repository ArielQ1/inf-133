import requests


#Definir la consulta
query = """ 
    {
        hello
        goodbye
    }
"""


#Definir a URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)