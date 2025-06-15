class Employee:
	def __init__(self, name, salary):
		self.name = name 
		self.salary = salary

class Manager(Employee):

	def __init__(self, name, salary, emp_list: list):
		super().__init__(name, salary)
		self.employee = emp_list

	def display(self):
		print(f"Manager: {self.name}")
		print("Team:")
		for i in self.employee:
			print(f"Name: {i.name}")
			print(f"Salary: {i.salary}")


class Leader(Employee):

	def __init__(self ,name, salary, emp_list: list):
		super().__init__(name, salary)
		self.employee = emp_list

	def display(self):
		print(f"Team Leader: {self.name}")
		print("Team:")
		for i in self.employee:
			print(f"Name: {i.name}")
			print(f"Salary: {i.salary}")


manager_name = input("Enter manager name: ")
manager_salary = input("Enter manager salary: ")
num = int(input("Enter no.of employees under manager: "))
emp_list1 = []
for i in range(num):
	name = input(f"Enter employee {i + 1} name: ")
	salary = input(f"Enter employee {i + 1} salary: ")
	emp_list1.append(Employee(name,salary))
manager = Manager(manager_name, manager_salary, emp_list1)

leader_name = input("Enter team leader name: ")
leader_salary = input("Enter team leader salary: ")
num = int(input("Enter no. of employees under team leader: "))
emp_list2 = []
for i in range(num):
	name = input(f"Enter employee {i + 1} name: ")
	salary = input(f"Enter employee {i + 1} salary: ")
	emp_list2.append(Employee(name, salary))
leader = Leader(leader_name, leader_salary, emp_list2)

manager.display()
leader.display()
