a=[1,2,3,4,5,5,5,6,8,7,5]
m=[]
for i in a:
    if i not in m:
        m.append(i)
m.sort()
print("Second largest number: ",m[-2])