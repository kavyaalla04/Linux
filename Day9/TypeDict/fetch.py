#GET - fetch a user

import requests

BASE_URL = "https://jsonplaceholder.typicode.com/"

response = requests.get(f"{BASE_URL}/users/1")
print(response.status_code) #200
print(response.json())

#POST - create a new user
new_post = {"title": "Hello", "body": "world", "userId": 50}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
print(response.status_code) #201
print(response.json())

#PUT - entirely update a user
#PATCH - partially update a user
response = requests.patch(f"{BASE_URL}/posts/1", json={"title": "Updated Title: "})
print(response.status_code) #200
print(response.json())

#DELETE - delete a user
response = requests.delete(f"{BASE_URL}/posts/1")
print(response.status_code) #200
print(response.json()) #{} - empty response