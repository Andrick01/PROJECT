n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    r = input("Enter roll no: ")

    m = []
    for j in range(5):
        x = float(input("Enter mark: "))
        m.append(x)

    t = sum(m)
    avg = t / 5

    if avg >= 90:
        g = "A"
    elif avg >= 80:
        g = "B"
    elif avg >= 70:
        g = "C"
    elif avg >= 60:
        g = "D"
    elif avg >= 50:
        g = "E"
    else:
        g = "F"

    p = True
    for k in m:
        if k < 40:
            p = False
            break

    if p:
        s = "Pass"
    else:
        s = "Fail"

    print("Name:", name)
    print("Roll No:", r)
    print("Marks:", m)
    print("Total:", t)
    print("Average:", avg)
    print("Grade:", g)
    print("Result:", s)
    print()