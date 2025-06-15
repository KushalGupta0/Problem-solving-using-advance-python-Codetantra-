class Students:

    def __init__(self, name, l):
        self.name = name
        self.x = l[0]
        self.y = l[1]
        self.z = l[2]

    def compute(self):
        self.total = self.x + self.y + self.z
        self.average = self.total / 3

    def display(self):
        print("Name:", self.name)
        print("Marks:", [self.x, self.y , self.z])
        print("Total Marks:", self.total)
        print("Average Marks:", self.average)
        
name = input("Student name: ")
print("Enter marks: ")
l = []
for i in range(3):
    a = int(input())
    l.append(a)
student1 = Students(name , l)
student1.compute()
student1.display()
