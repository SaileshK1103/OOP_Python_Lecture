'''
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
'''

# Inheritance lecture
# Example 1: Single inheritance
'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"I am {self.name}, I am  {self.age} year old {self.gender} and my id is {self.id}"

class Student(Person):
    def __init__(self, name, age, gender,id):
        self.id = id
        super().__init__(name, age, gender)

    def introduce(self):
       return f"I am {self.name}, I am  {self.age} year old {self.gender} and my id is {self.id}"

# main program
student = Student("Ram", "Male", 30, 7 )
print(student.introduce())
'''
# Example 2: Multi level inheritance
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    def speak(self):
        return f"The Dog name is {self.name} and speaks Bhau Bhau"

# main program
dog = Dog("Happy")
print(dog.speak())
'''

# Example 3: Multi level inheritance

'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass

class Student(Person):
    def __init__(self, name, age, gender,student_id):
        self.student_id = student_id
        super().__init__(name, age, gender)

    def introduce(self):
       #return f"I am {self.name}, I am  {self.age} year old {self.gender} and my id is {self.student_id}
        pass

class Assistant(Student):
    def __init__(self, name, age, gender,student_id, salary):
        self.salary = salary
        super().__init__(name, age, gender, student_id)

    def introduce(self):
        return f"I am {self.name}, I am  {self.age} year old {self.gender} and my student id is {self.student_id} and assistant id is {self.salary}"


# main program
assistant = Assistant("Ram", 30, "Male", 1, 3000)
print(assistant.introduce())
'''
# Example 4 : Hierarchical inheritance
'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass

class Student(Person):
    def __init__(self, name, age, gender,student_id):
        self.student_id = student_id
        super().__init__(name, age, gender)

    def introduce(self):
       #return f"I am {self.name}, I am  {self.age} year old {self.gender} and my id is {self.student_id}
        pass

class Assistant(Student):
    def __init__(self, name, age, gender,student_id, salary):
        self.salary = salary
        super().__init__(name, age, gender, student_id)

    def introduce(self):
        return f"I am {self.name}, I am  {self.age} year old {self.gender} and my student id is {self.student_id} and assistant id is {self.salary}"

class Teacher(Person):
    def __init__(self, name, age, gender, teacher_title):
        self.teacher_title = teacher_title
        super().__init__(name, age, gender)

    def introduce(self):
        return f"I am {self.name}, I am  {self.age} year old {self.gender} and my teacher title is {self.teacher_title}"

# main program

teacher = Teacher("Ram", "Male", 30, "Python")

print(teacher.introduce())
'''
'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        pass

class Teacher(Person):
    def __init__(self, name, age, gender, title):
        super().__init__(name, age, gender)
        self.title = title
    def introduce(self):
        pass

class Assistant(Teacher):
    def __init__(self,name, age, gender,title,salary):
        super().__init__(name, age, gender, title)
        self.salary = salary

    def introduce(self):
        return f"I am {self.name}, I am  {self.age} year old {self.gender} and my salary is {self.salary}"

class part_time_teacher(Teacher):
    def __init__(self,name, age, gender,title, hour):
        super().__init__(name, age, gender,title)
        self.hour = hour

    def introduce(self):
        return f"I am {self.name}, I am  {self.age} year old {self.gender} and my teacher title is {self.title}"

# main program
assistant = Assistant("Ram", "Male", 30, "Python", 3000)
print(assistant.introduce())
part_time_teacher = part_time_teacher("Ram", "Male", 30, "Python", 3)
print(part_time_teacher.introduce())
'''

'''
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args = request.args
    try:
        num1 = float(args.get('num1', 0))
        num2 = float(args.get('num2', 0))
        total_sum = num1 + num2
        return str(total_sum)
    except(TypeError, ValueError):
        return "Invalid Input: *Please enter a valid number",400
if __name__ == '__main__':
    app.run(host='127.0.0.1', port= 5000, debug=True, use_reloader=False)
'''