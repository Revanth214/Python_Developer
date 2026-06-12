a=[1,2,3,4,5,6,7,4,3,2,1]
m=[]
for i in a:
    if i not in m:
        m.append(i)
print("Cleaned list of elements: ",m)