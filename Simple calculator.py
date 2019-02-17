# SIMPLE CALCULATOR 
print("Welcome to Simple Calculator")
x=int(input("Enter First no:"))
y=int(input("Enter Second no:"))
print("\nEnter 1 for Addition Enter 2 for Subtraction 3 for multiply 4 for divide")
z=int(input("the option is:"))

if(z==1):
    sum=x+y
    print("The sum is ",sum)
if(z==2):
    subtraction=x-y
    print("The subtraction is:",subtraction)
if(z==3):
    product=x*y    
    print("The product is:",product)
if(z==4):
    divide=x/y
    print("The division is:",divide)
    
    
    
    
    
    