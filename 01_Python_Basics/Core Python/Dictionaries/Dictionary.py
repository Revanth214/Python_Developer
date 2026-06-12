# Creating dictionaries
my_dict={}
print(my_dict)
my_dict=dict(apple=1, banana=2, orange=5)
print(my_dict)
my_dict=dict([('apple',5),('banana',5),('Guo',25)])
print(my_dict)

# accessing values

print(my_dict['apple'])
print(my_dict['banana'])
# use .get() if you want a default when the key is missing
print(my_dict.get('Guo'))
print(my_dict.get('orange', 'not found'))