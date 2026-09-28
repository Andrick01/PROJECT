a=input("Enter a string:")
c=""
for i in a:
    if i in " ":
        continue
    else:
        c+=i
print(c)