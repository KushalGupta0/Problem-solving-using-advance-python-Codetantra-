'''
Partial code given for your reference.
Implementation requirements are also mentioned in the statement.
'''
class EvenNumbers:
    # Define the class
	def __init__(self, limit):
		self.a = 0
		self.limit =  limit

	def __iter__(self):
		return self

	def __next__(self):
		if self.a > self.limit:
			raise StopIteration
		num = self.a
		self.a += 2
		return num
# Get user input for the limit
limit = int(input("Enter the limit: "))
# Create the EvenNumbers iterator with user input limit
iterator = EvenNumbers(limit)
# Print each even number up to the user input limit
for i in iterator:
	print(i) 
