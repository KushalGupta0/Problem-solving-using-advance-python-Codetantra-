# Base class A
class A:
	def __init__(self, a):
		self.a = a

	def display(self):
		print(self.a)

# Base class B
class B:
	def __init__(self, b):
		self.b = b

	def display(self):
		print(self.b)

# Derived class C that inherits from A and B
class C(A, B):
	def __init__(self, a, b, c):
		A.__init__(self, a)
		B.__init__(self, b)
		self.c = c

# Derived class D that inherits from C and A
class D(C, A):
	def __init__(self, a, b, c, d):
		super().__init__(a, b, c)
		self.d = d

	def display(self):
		print(f"D: {self.d}")

# Derived class E that inherits from C and B
class E(C, B):
	def __init__(self, a, b, c, e):
		super().__init__(a, b, c)
		self.e = e

	def display(self):
		print(f"E: {self.e}")

# Take user input for the values of a, b, c, d, and e
a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))
c = int(input("Enter value for C: "))
d = int(input("Enter value for D: "))
e = int(input("Enter value for E: "))

# Create objects of classes D and E and Call display() method for each object to demonstrate hybrid inheritance
obj_d = D(a, b, c, d)
obj_e = E(a, b, c, e)

obj_d.display()
obj_e.display()

# Print MRO for each class, for order please refer the visible test cases.
print(f"MRO for class D: {list(D.__mro__)}")
print(f"MRO for class E: {list(E.__mro__)}")
print(f"MRO for class C: {list(C.__mro__)}")
print(f"MRO for class A: {list(A.__mro__)}")
print(f"MRO for class B: {list(B.__mro__)}")
