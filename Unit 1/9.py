class Numbers:

	def __init__(self):
		pass

	def insert_elements(self):
		l = []
		num = int(input("Enter no.of elements:"))
		for i in range(num):
			a = int(input())
			l.append(a)
		self.value = l

	def find_max(self):
		return max(self.value)

n1 = Numbers()
n1.insert_elements()
print("The largest number is:", n1.find_max())
