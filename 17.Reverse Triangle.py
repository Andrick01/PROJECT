n=int(input("Enter no of rows:"))
a=0
for i in range(n,0,-1):
    for j in range(i):
        print("* ",end="")
    print()
    a+=1
    print("  "*a,end="")