def p(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = int(input("Enter a number: "))
if p(x):
    print(x, "is a prime number")
else:
    print(x, "is not a prime number")