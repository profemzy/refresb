students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readline():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


def print_student_list():
    print(students)


def check_continuity():
    print("Do you want to add a student?")
    resp = input("If YES PRESS  'Y' and 'N' if  NO:  ")
    return resp


while True:
    response = check_continuity()

    if response == 'Y':
        read_file()
        print_students_titlecase()

        student_name = input("Enter Student Name: ")
        student_identification = input("Enter Student ID: ")
        try:
            student_id = int(student_identification)
            add_student(student_name, student_id)
            save_file(student_name)
            print_student_list()

        except:
            print("Invalid Student ID!!")

    elif response == 'N':
        break
    else:
        break

print("Thank You")
