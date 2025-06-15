class Complex:
        
    # Define class Complex with required methods
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"

    def __sub__(self, other):
        return f"{self.real - other.real} + {self.imaginary - other.imaginary}i"

    def __mul__(self, other):
        a = self.real 
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return f"{a*c - b*d} + {a*d + b*c}i"

    def __truediv__(self, other):
        den = other.real ** 2 + other.imaginary ** 2
        a = self.real 
        b = self.imaginary
        c = other.real
        d = other.imaginary
        return f"{(a*c + b*d)/den} + {(b*c - a*d)/den}i"

# Prompt the user to enter complex numbers
while True:
    try:
        real1 = float(input("Enter the real part of the first complex number: "))
        imag1 = float(input("Enter the imaginary part of the first complex number: "))
        real2 = float(input("Enter the real part of the second complex number: "))
        imag2 = float(input("Enter the imaginary part of the second complex number: "))
        c1 = Complex(real1, imag1)
        c2 = Complex(real2, imag2)
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Define class 
print(c1 + c2)  # Output: sum of the two complex numbers
print(c1 - c2)  # Output: difference of the two complex numbers
print(c1 * c2)  # Output: product of the two complex numbers
print(c1 / c2)  # Output: division of the two complex numbers

c1 += c2
print(c1)  # Output: updated value of c1