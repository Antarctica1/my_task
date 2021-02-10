n=[]

for i in range(3):
    n.append(int(input()))

result=n[0]*n[1]*n[2]
d=str(result)


for i in range(10):
    print(d.count(str(i)))