'''
Partial code is given below,
Follow the problem requirements given.
'''
# Define Employee class

class Employee:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def display_personal_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)
        print("Phone: ", self.phone)

#define SalaryEmployee as a derived class from Employee class
class SalaryEmployee(Employee):

    def __init__(self, name, age, address, phone, salary):
        super().__init__(name, age, address, phone)
        self.salary = salary

    def display_salary_info(self):
        super().display_personal_info()
        print("Salary: ", self.salary)

# Creating a list to store 5 instances of the SalaryEmployee class
employees = []

# Taking input of employee records from the user
for i in range(5):
    print("Enter details of employee #", i+1)
    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")
    phone = input("Phone: ")
    salary = int(input("Salary: "))
# Creating instance of SalaryEmployee class and adding it to the list
    emp = SalaryEmployee(name, age, address, phone, salary)
    employees.append(emp)
# Displaying personal and salary information for each employee
for i in employees:
    i.display_salary_info()
