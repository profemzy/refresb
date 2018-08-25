students = []


class Student:

    # Class Attribute, same across all instances of that class
    school_name = "SteinServe Academy"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student: " + self.name

    def get_capitalized_name(self):
        return self.name.capitalize()


student = Student("Dare", 876)
print(student.get_capitalized_name())
