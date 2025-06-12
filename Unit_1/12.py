class Complex:
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary

    def display(self):
        sign = '+' if self.imag >= 0 else '-'
        print(f"{self.real} {sign} {abs(self.imag)}i")

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)




while True:
    print("Select an option:")
    print("1. Read two complex numbers")
    print("2. Display two complex numbers")
    print("3. Add two complex numbers")
    print("4. Subtract two complex numbers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        a = float(input("Enter the real part of the first complex number: "))
        b = float(input("Enter the imaginary part of the first complex number: "))
        c = float(input("Enter the real part of the second complex number: "))
        d = float(input("Enter the imaginary part of the second complex number: "))
        c1 = Complex(a, b)
        c2 = Complex(c, d)

    elif choice == '2':
        print("First complex number:")
        c1.display()
        print("Second complex number:")
        c2.display()

    elif choice == '3':
        result = c1 + c2
        print("Sum of the two complex numbers:")
        result.display()


    elif choice == '4':
        result = c1 - c2
        print("Difference of the two complex numbers:")
        print(f"{result.real} + {result.imag}i")

    else:
        break
