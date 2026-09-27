a=int(input("Enter the number:"))
if a==0:
    print("The factorical of 0 is 1")
fact=1
for i in range(1,a+1):
    fact*=i
print("Factorial of ",a,"is ",fact)