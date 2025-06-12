class Temperature:

	def __init__(self, temperature):
		self.temperature = temperature

	def convert_to_fahrenhiet(self):
		return list(map(lambda x: (x * 9/5)+ 32, self.temperature))

celsius = input("Enter a list of temperatures in Celsius: ")
celsius = celsius.split(" ")
celsius = [float(i) for i in celsius]
temp = Temperature(celsius)
print("Temperatures in Fahrenheit: ", temp.convert_to_fahrenhiet())
