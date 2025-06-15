import math

class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = []

    def get_dimensions(self):
        for i in range(self.num_sides):
            length = float(input(f"Enter length of side {i + 1}: "))
            self.sides.append(length)

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def area(self):
        return self.sides[0] * self.sides[1]

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
# Prompt user for dimensions of rectangle
print("Dimensions of rectangle")
rect = Rectangle()
rect.get_dimensions()
print(f"Area of rectangle: {rect.area():.2f}")

# Prompt user for dimensions of triangle
print("Dimensions of triangle")
tri = Triangle()
tri.get_dimensions()
print(f"Area of triangle: {tri.area():.2f}")