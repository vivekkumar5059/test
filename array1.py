x=int(input("enter size "))
arr=[0] * x
for i in range(x):
    arr[i]=int(input())

print(arr)
sum=0
for i in range(x):
    sum = arr[i] + sum


print(sum)
