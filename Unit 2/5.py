# Comment out already written code and then copy this
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Enter name of a person:")
age = input("Enter age of a person:")
obj = Person(name, age)

while True:
    print("Select an option:")
    print("1. Check if person object has an attribute")
    print("2. Get value of a person object attribute")
    print("3. Set value of a person object attribute")
    print("4. Delete an attribute from person object")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        attr_name = input("Enter the attribute name to check: ")
        if hasattr(obj, attr_name):
            print(f"The person object has a '{attr_name}' attribute")
        else:
            print(f"The person object does not have a '{attr_name}' attribute")
            
    elif choice == "2":
        attr_name = input("Enter the attribute name to get: ")
        print(f"The value of the '{attr_name}' attribute is: {getattr(obj, attr_name)}")

    elif choice == "3":
        attr_name = input("Enter the attribute name to set: ")
        attr_value = input("Enter the new value: ")
        setattr(obj, attr_name, attr_value)
        print(f"The value of the '{attr_name}' attribute is now: {attr_value}")
        
    elif choice == "4":
        attr_name = input("Enter the attribute name to delete: ")
        delattr(obj, attr_name)
        print(f"The '{attr_name}' attribute has been deleted from the person object")

    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again")

