#Calculate the factorial using functions
x=int(input("Enter the no to find the find factorial:"))
def fact(n):
    if n==1:
        return(n)
    else:
        return(n*fact(n-1))
 
print("The Factorial is:",fact)       