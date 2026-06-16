import requests

resposnse=requests.get("https://jsonplaceholder.typicode.com/users/1")

data=resposnse.json()
print(resposnse.text)
print(data["name"])
print(data["phone"])
print(data["company"]["name"])
print(data["address"]["geo"]["lat"])