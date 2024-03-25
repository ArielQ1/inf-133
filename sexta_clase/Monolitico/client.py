import requests
url = "http://localhost:8000"
print("-----------------")

response = requests.get(f"{url}/post/2")
print(response.text)

print("-----------------")

response_post = url + "/posts"
nuevo_post = {
    "title": "Mi experiencia como dev",
}
response = requests.post(f"{url}/posts", data=nuevo_post)

print("-----------------")

put_data = {
     "content": "En progreso"
}
response = requests.put(f"/post/{3}", data=put_data)