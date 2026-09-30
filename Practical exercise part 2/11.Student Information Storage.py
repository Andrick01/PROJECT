d = {}

d["name"] = input("Enter student name: ")
d["roll"] = input("Enter roll number: ")
d["marks"] = input("Enter marks: ")

print("Student Details:")
for k in d:
    print(k, ":", d[k])