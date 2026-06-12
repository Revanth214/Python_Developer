a={1,2,3,4,5,4,6,5,3,2}
a.add(9)
print("Set adding: ", a)
a.remove(3)
print("set element remove: ", a)
b={6,4,10,23,5,4,3}
c=a.union(b)
print("set union: ", c)
d=a.difference(b)
print("Set differencce: ", d) # Returns elements in the first set that are not in the second.
e=a.intersection(b)
print("set intersection: ", e) # Returns only elements common to both sets.