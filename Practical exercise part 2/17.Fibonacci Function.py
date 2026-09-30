def fib(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()

x = int(input("Enter how many terms: "))
fib(x)