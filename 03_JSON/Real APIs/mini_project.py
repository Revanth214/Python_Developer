import requests

user_id = input("Enter User ID: ")

response = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{user_id}"
)

data = response.json()

print("Name:", data.get("name"))
print("Email:", data.get("email"))
print("City:", data.get("address", {}).get("city"))