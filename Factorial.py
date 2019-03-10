#Calculate the factorial using functions
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
    
x=int(input("Enter the no. to find factorial:"))
result=fact(x)    
print("The factorial of",x,"is",result)    
       