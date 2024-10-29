class Student:
    department = "Faculty of Science and Technology"
    count = 0
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.courses = []
    def __str__(self):
        return f"The name of student is {self.name}, gender is {self.gender}, age is {self.age}"
    def get_name(self):
        return self.name
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age
    def add_course(self, course):
        self.courses.append(course)

class Course:
    def __init__(self):
        self.students = []
    def addStudent(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to the list")
    def removeStudent(self, student):
        self.students.remove(student)
        print(f"{student.name} has been removed from the list")

    def getStudents(self):
        for student in self.students:
            print(student)

# main program
student1 = Student("Sailesh", "Male", 30)
student2 = Student("Ram", "Male", 25)
student3 = Student("Sita", "Female", 29)
course = Course()
course.addStudent(student1)
course.addStudent(student2)
course.addStudent(student3)
course.getStudents()
