class Person:
    def __init__(self, name = "John Smith", age = 35):
        self.name = name 
        self.age = age
    def __del__(self):
        print("{} has been deleted".format(self.name))

name = input("Enter name: ")
age = int(input("Enter age: "))

p1 = Person()
p2 = Person(name, age)

print("{} is {} years old".format(p1.name, p1.age))
print("{} is {} years old".format(p2.name, p2.age))

del p1
del p2