import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# GET /chocolates
response = requests.get(url=url)
print(response.json())

# POST /chocolates
new_chocolate_data = {
    "chocolate_type": "bombon",
    "peso": "25 g",
    "sabor": "sandia",
    "relleno": "aguado"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "tableta",
    "peso": "25 g",
    "sabor": "sandia"
}


response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())

# PUT /chocolates/{chocolate_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "peso": "85 gr"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())

# DELETE /chocolate/{chocolate_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())