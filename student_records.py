students = []


def add_student(name, roll_no, department):
    student = {
        "name": name,
        "roll_no": roll_no,
        "department": department
    }

    students.append(student)
    print("Student record added successfully.")


def view_students():
    if not students:
        print("No student records available.")
        return

    print("\nStudent Records")
    print("----------------")

    for student in students:
        print(
            f"Name: {student['name']} | "
            f"Roll No: {student['roll_no']} | "
            f"Department: {student['department']}"
        )


def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}")
            print(f"Department: {student['department']}")
            return

    print("Student not found.")


def count_students():
    print(f"Total Students: {len(students)}")


def main():
    print("\n=== Student Management System ===")
    while True:
        print("\nStudent Records")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Count Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            department = input("Enter department: ")

            add_student(name, roll_no, department)

        elif choice == "2":
            view_students()

        elif choice == "3":
            roll_no = input("Enter roll number: ")
            search_student(roll_no)

        elif choice == "4":
            count_students()

        elif choice == "5":
            print("Exiting Student Records.Goodbye")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
