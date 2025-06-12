import math

class Fraction:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1  

    def getdata(self):
        self.numerator = int(input("Enter numerator: "))
        self.denominator = int(input("Enter denominator: "))
        
    def show(self):
        gcd = math.gcd(self.numerator, self.denominator)
        simplified_num = self.numerator // gcd
        simplified_den = self.denominator // gcd

        print(f"{simplified_num}/{simplified_den}")

c = Fraction()
c.getdata()
c.show()
