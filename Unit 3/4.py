'''
Partial code given for your reference.
Implementation requirements are also mentioned in the statement.
'''
class Squares:
   # Define class as required
	def __init__(self, limit):
		self.a = 0
		self.limit = limit

	def __iter__(self):
		return self

	def __next__(self):
		if self.a > self.limit:
			raise StopIteration
		num = self.a
		self.a += 1
		return num ** 2

# Get user input for the limit
limit = int(input("Enter the limit: "))
# Create the Squares iterator with user input limit
iterator = Squares(limit)
# Print each square up to the user input limit
for i in iterator:
	print(i) 
