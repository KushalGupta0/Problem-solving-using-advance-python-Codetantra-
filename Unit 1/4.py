class Employee:
	list_of_emp = []
	def __init__(self, name, designation, salary):
		self.name = name
		self.designation = designation
		self.salary = salary
		Employee.list_of_emp.append(self)

	@classmethod
	def getdata(cls):
		for i in Employee.list_of_emp:
			print("Name:", i.name)
			print("Designation:", i.designation)
			print("Salary:", i.salary)

	@classmethod
	def average(cls):
		total = 0
		for i in Employee.list_of_emp:
			total += i.salary
		return total / len(Employee.list_of_emp)

num = int(input("Enter no.of employees: "))
for i in range(num):
	name = input("Enter employee name: ")
	designation = input("Enter employee designation: ")
	salary = float(input("Enter employee salary: "))
	Employee(name, designation, salary)

Employee.getdata()
print("Average salary:", Employee.average())
