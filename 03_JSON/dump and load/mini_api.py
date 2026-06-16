import json
data={
    "user": {
        "name": "Rama",
        "email": "rama@gmail.com"
    },
    "posts": [
        {
            "title": "Python",
            "likes": 100
        }
    ]
}
with open("mini_api.json", "w") as file :
    json.dump(data, file)

with open("mini_api.json", "r") as file :
    info=json.load(file)

print(info["posts"][0]["title"])