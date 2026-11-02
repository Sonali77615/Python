class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

student1 = Student("Rahul", 20, 85)
print("Student Name:", student1.name)
print("Student Age:", student1.age)
print("Student Marks:", student1.marks)