class Person:
	# define the class as required for > overloading
	def __init__(self, name, age):
		self.name = name 
		self.age = age

	def __gt__(self, other):
		return self.age > other.age

	def __eq__(self, other):
		return self.age == other.age

# User input
person1_name = input("Name of person 1: ")
person1_age = int(input("Age of person 1: "))
person2_name = input("Name of person 2: ")
person2_age = int(input("Age of person 2: "))

# Create person objects
person1 = Person(person1_name, person1_age)
person2 = Person(person2_name, person2_age)

# Compare age of persons, for print messages refer the test cases visible
if person1 > person2:
	print(f"{person1.name} is older than {person2.name}.")

elif person1 == person2:
	print(f"{person1.name} {person2.name} are of same age.")

else:
	print(f"{person2.name} is older than {person1.name}.")
