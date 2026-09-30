n = int(input("Enter number of employees: "))
d = {}

for i in range(n):
    k = input("Enter employee ID: ")
    v = input("Enter employee name: ")
    d[k] = v

print("Employee Records:")
for k in d:
    print("ID:", k, "Name:", d[k])

s = input("Enter ID to search: ")
if s in d:
    print("Found employee:", d[s])
else:
    print("Not found")