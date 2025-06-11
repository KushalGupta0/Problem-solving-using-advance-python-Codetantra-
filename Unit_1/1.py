class Rectangle:

    def __init__(self, length, width):
        self.length = length 
        self.width = width 

    def area(self):
        return self.length * self.width


length = int(input("Enter the length"))
width = int(input("Enter the width"))

rectangle1 = Rectangle(length, width)

area_rect1 = rectangle1.area()
print(area_rect1)