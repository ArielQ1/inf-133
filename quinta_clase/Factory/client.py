# Importamos la biblioteca requests para hacer peticiones HTTP
import requests

# Definimos la URL del servicio al que vamos a hacer la petición
url = "http://localhost:8000/delivery"

headers = {"Content-Type": "application/json"}
vehicle_type = "motorcycle"
data = {"vehicle_type": vehicle_type}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling delivery:", response.text)


vehicle_type = "drone"
data = {"vehicle_type": vehicle_type}
if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling delivery:", response.text)
response = requests.post(url, json=data, headers=headers)

vehicle_type = "scout"
data = {"vehicle_type": vehicle_type}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print(response.text)
else:
    print("Error scheduling delivery:", response.text)
