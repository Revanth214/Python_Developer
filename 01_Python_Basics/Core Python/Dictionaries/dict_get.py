# dict.get(key, default) returns the value for key if it exists, otherwise it returns default
my_dict=dict(apple=1, banana=3, orange=5, leo=10)
a=my_dict.get('apple')
print(a)

person = {"name": "Guo", "age": 25}

print(person.get("name"))          # Guo
print(person.get("age"))           # 25
print(person.get("city"))          # None
print(person.get("city", "N/A"))   # N/A