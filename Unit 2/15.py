# import math module for PI
import math
# Define the base class Shape
class Shape:
    def __init__(self, radius):
        self.radius = radius

# Define the derived class Circle that inherits from Shape
class Circle(Shape):
	# define constructor and area method, 
	# Make use of super to initiate base class (Shape) constructor.
    def __init__(self, radius):
        super().__init__(radius)
    
    def area(self):
        return math.pi * self.radius ** 2

# Define the derived class Cone that inherits from Shape
class Cone(Shape):
	# define constructor and area method, 
	# Make use of super to initiate base class (Shape) constructor.
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def area(self):
        slant_height = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * (self.radius + slant_height)
# Take user input for the radius and height of the circle and cone
radius = float(input("Radius: "))
height = float(input("Height: "))

# Create objects of classes Circle and Cone using user input
circle_obj = Circle(radius)
cone_obj = Cone(radius, height)

# Print the area of the circle and cone using the area() method of each object
print(f"Area of the circle = {circle_obj.area():.2f}")
print(f"Area of the cone = {cone_obj.area():.2f}") 
