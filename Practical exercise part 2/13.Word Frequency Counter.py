t = input("Enter a sentence: ")
w = t.split()
d = {}

for i in w:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print("Word counts:")
for k in d:
    print(k, ":", d[k])