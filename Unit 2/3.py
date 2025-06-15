class MyClass:
	"""
	A class representing a MyClass object, define methods mentioned in the problem.
	__str__(), __repr__(), __new__,__doc__, __dict__, __name__ and __bases__ 
	
	"""
	def __new__(cls, *args, **kwargs):
		instance = super(MyClass, cls).__new__(cls)
		return instance

	def __init__(self, name , age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age} years old."

	def __repr__(self):
		return f"MyClass({self.name}, {self.age})"

	def __doc__(self):
		return type(self).__doc__

	def __dict__(self):
		return self.__dict__

	def __name__(self):
		return type(self).__name__

	def __bases__(self):
		return type(self).__bases__
	
# get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# create object
my_obj = MyClass(name, age)

# demonstrate __str__()
print(str(my_obj))
# demonstrate __repr__()
print(repr(my_obj))
# demonstrate __new__()
print(type(my_obj))
# demonstrate __doc__()
print(my_obj.__doc__)
# demonstrate __dict__()
print(my_obj.__dict__)
# demonstrate __name__()
print(my_obj.__name__)
# demonstrate __bases__()
print(my_obj.__bases__)