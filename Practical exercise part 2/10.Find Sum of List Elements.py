n = int(input("Enter how many numbers: "))
l = []
for i in range(n):
    x = int(input("Enter number: "))
    l.append(x)

s = 0
for i in l:
    s = s + i

print("Sum is:", s)