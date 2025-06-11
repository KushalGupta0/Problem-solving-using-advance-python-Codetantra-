class Temperature:

    def __init__(self, temperature):
        self.temperature = temperature

    def convert_to_fahrenheit(self):
        return list(map(lambda x: (x * 9/5) + 32, self.temperature))
    
celsius = input("Enter a list of temperature in celsius: ")
celsius = celsius.split(' ')
celsius = [float(i) for i in celsius]
temp = Temperature(celsius)
print("Temperature in Fahrenheit:", temp.convert_to_fahrenheit())