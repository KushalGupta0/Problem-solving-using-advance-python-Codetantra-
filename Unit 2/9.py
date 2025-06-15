class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
class Location:	
	def __init__(self, location, destination):
		self.location = location
		self.destination = destination

	def print_reflection(self):
		print(f"Original location: {self.location.x} {self.location.y}")
		print(f"Reflected location: {-self.location.x} {self.location.y}")

# Input from user
x1 = int(input("Enter x1 value of location: "))
y1 = int(input("Enter y1 value of location: "))
x2 = int(input("Enter x2 value of destination: "))
y2 = int(input("Enter y2 value of destination: "))

# Create Point objects
loc = Point(x1, y1)
dest = Point(x2, y2)

# Create Location object
place = Location(loc, dest)

# Call the reflection method
place.print_reflection()