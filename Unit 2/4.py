def inspect_object(obj):
	# Write code here, have clarity from the visible test case
	obj_type = type(obj)
	print(f"Type: {obj_type}")
	print(f"Is instance of MyClass? {isinstance(obj, MyClass)}")
	print(f"Is instance of str? {isinstance(obj, str)}")
	print(f"Is subclass of object? {issubclass(obj_type, object)}")
	print(f"Is callable? {callable(obj)}")
# MyClass is given below with a constructor
class MyClass:
	def __init__(self, value):
		self.value = value
 

# Driver code
while True:
	user_input = input("Enter an object to inspect (or 'q' to quit): ")
	if user_input == 'q':
		break
	try:
		# Write code here to make use of eval and inspect_object function.
		obj = eval(user_input)
		inspect_object(obj)
	except:
		print("Invalid input!")
