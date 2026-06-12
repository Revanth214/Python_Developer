n=[1,2,3,6,99,5,4,7,43,2,1]
m=0
for i in range(len(n)):
    if n[i]>m:
        m=n[i]
print("Laargest number in the list: ",m)