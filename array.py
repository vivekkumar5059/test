from audioop import reverse


x=[1 , 2 ,3 ,4 ,5 ,3 ,5 ,1 ,3 , 2]
print(x)
x.append(9)
print(x[0], x[1]  ,x[4])
print(x)
x.reverse()
print(x)
print(x.count(int(input())))
