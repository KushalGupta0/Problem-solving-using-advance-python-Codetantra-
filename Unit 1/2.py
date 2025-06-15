class Numbers:
# Define the class
    MULTIPLIER = 2

    def __init__(self, x , y) :
        self.x = x
        self.y = y 

    def add(self):
        return self.x + self.y
    
    @classmethod
    def multiply(cls, d):
        return cls.MULTIPLIER * d
    
    @staticmethod
    def subtract(b, c):
        return b - c
    
    def tup(self):
        return (self.x, self.y)
    
# Write driver code to access the class attributes

mul = int(input("Enter MULTIPLIER value:"))
x = int(input("Enter x value:"))
y = int(input("Enter y value:"))
d = int(input("Enter value to multiply:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))

num = Numbers(x,y)
Numbers.MULTIPLIER = mul
print("Sum:", num.add())
print("Product:", num.multiply(d))
print("subtraction:", num.subtract(b,c))
print("values:",num.tup())
