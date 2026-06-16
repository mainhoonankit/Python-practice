FILENAME = "students.txt"

def add_student():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    course = input("Enter course name: ").strip()

    if student_id == "" or name == "" or course == "":
        print("All fields are required.")
        return
    try:
        with open(FILENAME, "r") as file:
            for record in file:
                parts = record.strip().split(",")

                if len(parts) != 3:
                    continue

                existing_id = parts[0]

                if existing_id == student_id:
                    print("Student ID already exists.")
                    return

    except FileNotFoundError:
        pass

    with open(FILENAME, "a") as file:
        file.write(f"{student_id},{name},{course}\n")

    print("Student added successfully.")
    
def display_students():
    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()

        if len(records) == 0:
            print("No records found.")
            return

        for record in records:
            student_id, name, course = record.strip().split(",")
            print(f"ID: {student_id} | Name: {name} | Course: {course}")

    except FileNotFoundError:
        print("No records file found.")

def search_student():
    search_id = input("Enter student ID to search: ").strip()
    found = False

    try:
        with open(FILENAME, "r") as file:
            for record in file:
                student_id, name, course = record.strip().split(",")

                if student_id == search_id:
                    print(f"Found: {name} is enrolled in {course}")
                    found = True
                    break

        if found == False:
            print("Student not found.")

    except FileNotFoundError:
        print("No records file found.")

while True:
    print("\n===== Student Record File System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank you.")
        break
    else:
        print("Invalid choice.")