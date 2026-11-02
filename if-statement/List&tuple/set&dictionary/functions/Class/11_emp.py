class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("EEmployee Salary:", self.salary)

emp = Employee("Rahul", 30000) 

emp.display()   
            