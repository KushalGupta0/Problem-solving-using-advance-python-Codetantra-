'''
Partial code given for your reference.
Implementation requirements are also mentioned in the statement.
'''
def count_up_to_ten():
	# Raises Exception with message
	counter = 0
	while True:
		if counter != 10:
			yield(counter)
			counter += 1
		else: 
			raise ValueError("Counter has reached 10")

# Create the count up to ten generator
num = count_up_to_ten()

try:
	# Print each number in the sequence up to 10
	for i in num:
		print(i)
except  ValueError as e:# Prints message raised by Exception
	print(str(e)) 
