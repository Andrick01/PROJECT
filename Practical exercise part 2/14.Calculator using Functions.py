def a(x, y):
    return x + y

def s(x, y):
    return x - y

def m(x, y):
    return x * y

def d(x, y):
    return x / y

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
o = input("Enter operation (+, -, *, /): ")

if o == "+":
    print("Result:", a(x, y))
elif o == "-":
    print("Result:", s(x, y))
elif o == "*":
    print("Result:", m(x, y))
elif o == "/":
    print("Result:", d(x, y))
else:
    print("Invalid operator")