d = {}


def a():
    r = input("Enter register number: ")
    if r in d:
        print("Student already exists!")
        return
    n = input("Enter student name: ")
    m = []
    print("Enter marks for 5 subjects:")
    for i in range(5):
        x = float(input("Enter mark: "))
        m.append(x)
    d[r] = {"name": n, "marks": m}
    print("Student added successfully!")


def s():
    r = input("Enter register number to search: ")
    if r in d:
        print("Name:", d[r]["name"])
        print("Marks:", d[r]["marks"])
    else:
        print("Student not found!")


def u():
    r = input("Enter register number to update marks: ")
    if r in d:
        m = []
        print("Enter new marks for 5 subjects:")
        for i in range(5):
            x = float(input("Enter mark: "))
            m.append(x)
        d[r]["marks"] = m
        print("Marks updated successfully!")
    else:
        print("Student not found!")


def dl():
    r = input("Enter register number to delete: ")
    if r in d:
        del d[r]
        print("Student record deleted!")
    else:
        print("Student not found!")


def ds():
    if len(d) == 0:
        print("No student records to show!")
        return
    print("\n--- All Student Records ---")
    for k in d:
        print("Reg No:", k)
        print("Name:", d[k]["name"])
        print("Marks:", d[k]["marks"])
        print("---------------------------")


while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    c = input("Enter your choice (1-6): ")

    if c == "1":
        a()
    elif c == "2":
        s()
    elif c == "3":
        u()
    elif c == "4":
        dl()
    elif c == "5":
        ds()
    elif c == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please try again!")