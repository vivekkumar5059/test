



x= int(input())
y= int(input())

def min_step(x,y):
    count=0
    while x>1 or y> 1:
        if x>y:
            x=x-y
        elif y>x:
            y=y-x
        else:
            return -1
            
          

        
        count=count+1
    return count

print(min_step(x,y))


