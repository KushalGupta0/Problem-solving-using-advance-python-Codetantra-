# Use spaces instead of tab for indentation 
class Car:
    num_wheels = 4
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.make} is starting up...")


make = input("Enter make: ")
model = input("Enter model: ")
year = input("Enter year: ")

c1 = Car(make, model, year)

print("My car is a {} {} from {}".format(c1.make, c1.model, c1.year))
print("My car has {} wheels".format(c1.num_wheels))

c1.start()