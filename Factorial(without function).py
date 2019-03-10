#Calculate the factorial using functions
factorial=1
x=int(input("Enter the no to find the find factorial:"))
if x==1:
    print("The factorial of 1 is 1")
elif x<0:
    print("The Factorial does not exists for negative numbers")
elif x==0:    
    print("The factorial of 0 is 1")
elif x>0:
    for i in range(1,x+ 1):
       factorial = factorial*i
    print("The factorial of",x,"is",factorial)
else:
    print("You enter something irrevalent")    
       