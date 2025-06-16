'''
Use reduce() function from the functools module to calculate the sum of the first N natural numbers. 
The range() function is used to create a list of the numbers 1 through N. 
The reduce() function applies a lambda function that adds two numbers together to each element in the list. 
Finally, the program prints the sum of the first 10 natural numbers to the console.

'''
from functools import reduce
N = int(input("N: "))
iterator = range(1, N + 1)
print("Sum:", reduce(lambda x, y: x + y, iterator)) 
