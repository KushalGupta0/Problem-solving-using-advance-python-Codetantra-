class Fraction:
    '''
    Define all below listed functionalities
    def __init__(self, numerator, denominator): Constructor
    def __add__(self, other): Overload + operator
    def simplify(self): Simplify the fractions
    def __gcd(self, a, b): Compute GCD as utility function to simplify
    def __str__(self): String representation of the fraction
    '''

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self):
        gcd = self.__gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        return self  # for chaining if needed

    def __add__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Take user input for two fractions
numerator1 = int(input("Numerator of first fraction: "))
denominator1 = int(input("Denominator of first fraction: "))
numerator2 = int(input("Numerator of second fraction: "))
denominator2 = int(input("Denominator of second fraction: "))

# Create two Fraction objects from user input
fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)

# Add the two fractions using overloaded + operator
result = fraction1 + fraction2

# Simplify the result fraction using simplify() method
result.simplify()

# Print the result
print(f"{fraction1} * {fraction2} = {result}")
