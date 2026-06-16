import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response)

print(response.text)

print(response.json())

# 200 -> Success
# 404 -> Not Found
# 500 -> Server Error
# 403 -> Forbidden
#  401 Unauthorized
