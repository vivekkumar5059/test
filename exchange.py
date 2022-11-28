X=int(input())
def exchange(X):
   
   
    n=X

    z=0
    while X>0:
        Y=X % 10
        X= int(X / 10)
        z= int(z*10 + Y)
        
    if 0 ==z-n:
        print("paliardrom")    
    else:
        print("not pallidrom")
    print(z,n)        

print(exchange(X))
