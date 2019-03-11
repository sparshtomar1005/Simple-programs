#To print the fibonacci series for specified range using functions
first=0
second=1
x=int(input("Enter the no of fibonacci series you want:"))
for i in range(x):
    print(first)
    result = first
    first = second
    second = result+first
