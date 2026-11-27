students = []


def add_student(name, age, department):
    student = {
        "name": name,
        "age": age,
        "department": department
    }
    students.append(student)
    print("Student added successfully")


def display_students():
    if not students:
        print("No students found")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Age:", student["age"])
        print("Department:", student["department"])


def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Department:", student["department"])
            return

    print("Student not found")


def delete_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully")
            return

    print("Student not found")


def update_student(name, new_age, new_department):
    for student in students:
        if student["name"].lower() == name.lower():
            student["age"] = new_age
            student["department"] = new_department
            print("Student updated successfully")
            return

    print("Student not found")
