class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")

class Car(Vehicle):
    def __init__(self, make, model, year, price, num_doors):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors

    def details(self):
        super().details()
        print(f"Number of doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, price, engine_size):
        super().__init__(make, model, year, price)
        self.engine_size = engine_size

    def details(self):
        super().details()
        print(f"Engine size: {self.engine_size}")

class Truck(Vehicle):
    def __init__(self, make, model, year, price, payload_capacity):
        super().__init__(make, model, year, price)
        self.payload_capacity = payload_capacity

    def details(self):
        super().details()
        print(f"Payload capacity: {self.payload_capacity}")

# Main program
vehicle_type = input("Enter type of vehicle (c/m/t): ").lower()
make = input("Enter make of vehicle: ")
model = input("Enter model of vehicle: ")
year = int(input("Enter year of vehicle: "))
price = int(input("Enter price of vehicle: "))

if vehicle_type == 'c':
    num_doors = int(input("Enter number of doors of car: "))
    vehicle = Car(make, model, year, price, num_doors)
elif vehicle_type == 'm':
    engine_size = int(input("Enter engine size of motorcycle: "))
    vehicle = Motorcycle(make, model, year, price, engine_size)
elif vehicle_type == 't':
    payload_capacity = int(input("Enter payload capacity of truck: "))
    vehicle = Truck(make, model, year, price, payload_capacity)
else:
    print("Invalid vehicle type.")
    exit()

vehicle.details()