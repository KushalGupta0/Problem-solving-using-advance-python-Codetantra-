class Rectangle:

    def __init__(self, length, width):
        self.length = length 
        self.width = width 

    def area(self):
        return self.length * self.width


length = int(input("Enterlength: "))
width = int(input("Enter width: "))

rectangle1 = Rectangle(length, width)

area_rect1 = rectangle1.area()
print("Area of Rectangle:",area_rect1)
