n=int(input("Enter the value of n:"))
a,b=0,1
print("Fibonacci series:0 1 ",end="")
for i in range(2,n):
    print(a+b,end=" ")
    a,b=b,a+b
print()