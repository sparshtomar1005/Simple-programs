#CALCULATOR using elif
print("Welcome to simple calculator")
x=int(input("Enter first no:"))
y=int(input("Enter second no:"))

print("Choose an operation:\n1 for Addition \n2 for subtraction \n3 for multiplication \n4 for Division \n5 for modulus")
z=int(input("The option is :"))

if(z==1):
    print("sum=",x+y)
elif(z==2):
    print("subtraction=",x-y)
elif(z==3):
    print("product=",x*y)
elif(z==4):
    print("division=",x/y)
elif(z==5):
    print("remainder=",x%y)
else:
    print("You selected the wrong option:")
    
print("Thank you ,have a nice day")    