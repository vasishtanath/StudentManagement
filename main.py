import student

print("Welcome to Student Management System")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")

        student.add_student(name, age, department)

    elif choice == "2":
        student.display_students()

    elif choice == "3":
        name = input("Enter student name to search: ")
        student.search_student(name)

    elif choice == "4":
        name = input("Enter student name to delete: ")
        student.delete_student(name)

    elif choice == "5":
        name = input("Enter student name to update: ")
        age = int(input("Enter new age: "))
        department = input("Enter new department: ")

        student.update_student(name, age, department)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
