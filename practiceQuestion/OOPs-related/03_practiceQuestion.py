# Define Employee class with attirbutes role, department & salary. This class also has showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print("role = ", self.role)
        print("department = ", self.department)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",salary)

    def showDetailsEngineer(self):
        print("name = ", self.name)
        print("age = ", self.age)
        print("role = ", self.role)
        print("department = ", self.department)
        print("salary = ", self.salary)


Emp1 = Employee("Accountant","Finance","60,000")
Emp2 = Engineer("Karan", "24","75,000")
Emp1.showDetails()
print("")
print("Engineer employee")
print("")
Emp2.showDetailsEngineer()
