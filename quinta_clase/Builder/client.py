import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

pizza = {
    "tamaño": 100,
    "masa": "Grueso",
    "toppings": ["Carne", "Queso", "Tocino"]
}

response = requests.post(url, json=pizza, headers=headers)

print(response.json())