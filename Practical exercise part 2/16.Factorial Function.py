def f(n):
    a = 1
    for i in range(1, n + 1):
        a = a * i
    return a

x = int(input("Enter a number: "))
print("Factorial is:", f(x))