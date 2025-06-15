class Circle:
	PI = 3.14159

	def __init__(self, radius):
		self.radius = radius

	def area( self):
		return Circle.PI * self.radius ** 2

	def circum(self):
		return 2 * Circle.PI * self.radius

radius = int(input("Enter radius:"))
c1 = Circle(radius)
print("Radius:", c1.radius)
print("Area:", c1.area())
print("Circumference:", c1.circum())
