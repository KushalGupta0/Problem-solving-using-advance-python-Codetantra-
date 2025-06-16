'''
Take list of elements as input from the user,
and create a new list containing only the first letter of each element in the original list.
'''

existing_list = input("Enter a list of elements: ")
existing_list = existing_list.split(" ")

new_list = map(lambda x: x[0], existing_list)
new_list = list(new_list)
print(new_list) 
