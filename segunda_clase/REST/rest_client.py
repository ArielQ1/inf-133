import requests

url = "http://localhost:8000/"

#GET consulta a la ruta /lista_estudiantes 
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url = ruta_get)
#print(get_response.text)

#POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "id":2,
    "nombre": "Ghilmar",
    "apellido": "Valeriano",
    "carrera": "Desarrollo de Sotware",
}

ruta_post = url + "estudiantes?nombre=Fabricio"
get_response = requests.request(method="GET", url = ruta_get)
print(get_response.text)

post_response = requests.request(method="POST",
                                 url = ruta_post,
                                 json = nuevo_estudiante)


#print(post_response.text)