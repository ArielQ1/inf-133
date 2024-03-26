import requests

url =  "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

#GET /tacos
response = requests.get(url)
print(response.json())

#POST /tacos
mi_taco = {
    "base": "Grande",
    "guiso": "Salsa de Tomate",
    "toppings": ["Jamon", "Queso"],
    "salsa": "Roja"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

#GET /tacos
response = requests.get(url)
print(response.json())

#PUT /tacos/1

edit_taco = {
    "base": "Mediana",
    "guiso": "frio",
    "toppings": ["Carne", "Salchi"],
    "salsa": "Aguacate"
}
response = requests.put(url+"/1", json=edit_taco, headers=headers)
print(response.json())

#GET /tacos
response = requests.get(url)
print(response.json())

#DELETE /tacos/1

response = requests.delete(url+"/1")
print(response.json())

#GET /tacos
response = requests.get(url)
print(response.json())