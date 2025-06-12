class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @classmethod
    def midpoint(cls, p1, p2):
        return ((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    
    @classmethod
    def length(cls, p1, p2):
        return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5
    
x1 = float(input("Enter x1 value: "))
y1 = float(input("Enter y1 value: "))
x2 = float(input("Enter x2 value: "))
y2 = float(input("Enter y2 value: "))
p1 = Point(x1, y1)
p2 = Point(x2, y2)
print("Midpoint:", Point.midpoint(p1, p2))
print("Length:", format(Point.length(p1, p2),".2f"))
