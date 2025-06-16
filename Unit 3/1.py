'''
Partial code given for your reference.
Implementation requirements are also mentioned in the statement.
'''
def fibonacci(limit):
	a, b = 0, 1
	while a <= limit:
		yield(a)
		a , b = b, a + b
# Get the user input for the limit
limit = int(input("Enter the limit: "))

# Create the Fibonacci sequence generator
gen = fibonacci(limit)

# Print the Fibonacci sequence up to the user-specified limit
print("Fibonacci sequence up to {}: ".format(limit))
for i in gen:
	print(i) 
