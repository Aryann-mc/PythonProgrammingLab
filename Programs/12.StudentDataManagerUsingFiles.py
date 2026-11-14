#Student data manager using file operations
FILE_NAME = "students.txt"


def add_student():
    name = input("Student name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{grade}\n")
    print("Student saved.")


def show_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
        if not records:
            print("No student records yet.")
        else:
            print("\nName | Age | Grade")
            for record in records:
                print(record.strip().replace(",", " | "))
    except FileNotFoundError:
        print("No student records yet.")

def remove_student():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            if not records:
                print("No student records yet.")
            else:
                with open(FILE_NAME, "w+") as file:
                    name = input("Student name to be removed: ")
                    for i in records:
                        if name in i:
                            records.remove(i)
                    file.seek(0)
                    file.writelines(records)
                    print("Student removed.")
    except FileNotFoundError:
        print("No student records yet.")


while True:
    print("\n1. Add student\n2. Show students\n3. Remove student\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        break
    else:
        print("Please enter 1, 2, or 3.")
