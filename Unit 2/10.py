class Student:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def display(self):
		print(f"Name: {self.name}")
		print(f"Age: {self.age}")

class Marks(Student):
	def __init__(self, name, age, marks1, marks2, marks3):
		super().__init__(name, age)
		self.marks1 = marks1
		self.marks2 = marks2
		self.marks3 = marks3

	def display(self):
		super().display()
		print(f"Marks1: {self.marks1}")
		print(f"Marks2: {self.marks2}")
		print(f"Marks3: {self.marks3}")

class Result(Marks):
	def __init__(self, name, age, marks1, marks2, marks3):
		super().__init__(name, age, marks1, marks2, marks3)
		self.total = marks1 + marks2 + marks3

	def display(self):
		super().display()
		print(f"Total: {self.total}")

name1 = input("Enter student name: ")
age1 = input("Enter student age: ")
student1 = Student(name1, age1)
student1.display()

name2 = input("Enter student name: ")
age2 = input("Enter student age: ")
marks1 = int(input("Enter marks for subject1: "))
marks2 = int(input("Enter marks for subject2: "))
marks3 = int(input("Enter marks for subject3: "))
student2 = Marks(name2, age2, marks1, marks2, marks3)
student2.display()

name3 = input("Enter student name: ")
age3 = input("Enter student age: ")
marks1 = int(input("Enter marks for subject1: "))
marks2 = int(input("Enter marks for subject2: "))
marks3 = int(input("Enter marks for subject3: "))
student3 = Result(name3, age3, marks1, marks2, marks3)
student3.display()