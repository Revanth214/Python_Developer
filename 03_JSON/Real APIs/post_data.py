import requests

user_data = {
    "name": "Revanth",
    "skill": "Python developer"
}

response = requests.post(
    "https://reqres.in/api/users",
    json=user_data
)

print(response.status_code)
data = response.json()

print(data["error"])
