class MyDataStructure:
# define the class as mentioned in the implementation requirements
    def __init__(self, data):
        self.data = data

    def __contains__(self, search_element):
        return search_element in self.data
    

# Ask user to input their data structure
data_structure_type = input("Type of data structure do you want to create(list/dict/set): ").strip().lower()

if data_structure_type == "list":
    l = input("List(comma separated): ")
    lst = l.split(",")
    my_data_structure = MyDataStructure(lst)

elif data_structure_type == "dict":
    d = input("Key-value pairs of the dictionary(key1:value1,key2:value2,...): ")
    items = d.split(",")
    dict1 = {}
    for item in items:
        key_value = item.split(":")
        if len(key_value) == 2:
            key, value = key_value
            dict1[key.strip()] = value.strip()
    my_data_structure = MyDataStructure(dict1)

elif data_structure_type == "set":
    s = input("Set(comma separated): ")
    set1 = set(s.split(","))
    my_data_structure = MyDataStructure(set1)

else:
    print("Invalid type!")
    exit()

# Ask user to input the element to search for
search_element = input("Enter the element to search: ")

# Check if the element is present in the data structure
if search_element in my_data_structure:
    print(f"{search_element} is present in the {data_structure_type}")
else:
    print(f"{search_element} is not present in the {data_structure_type}")