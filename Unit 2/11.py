class Distance:
	def __init__(self, km, meters):
		self.km = km 
		self.meters = meters

	def display(self):
		return f"{self.km}km {self.meters}m"

class School:
	def __init__(self, name, distance):
		self.name = name 
		self.distance = distance

	def display(self):
		return f"Distance from house to {self.name} is {self.distance.display()}"

class Office:
	def  __init__(self, name, distance):
		self.name = name
		self.distance = distance

	def display(self):
		return f"Distance from house to {self.name} is {self.distance.display()}"


school_name = input("Enter the school name: ")
km1 = int(input("Enter the distance from house to school in kilometers: "))
m1 = int(input("Enter the distance from house to school in meters: "))
school_distance = Distance(km1, m1)
school = School(school_name, school_distance)

office_name = input("Enter the office name: ")
km2 = int(input("Enter the distance from house to office in kilometers: "))
m2 = int(input("Enter the distance from house to office in meters: "))
office_distance = Distance(km2, m2)
office = School(office_name, office_distance)

print(school.display())
print(office.display())
