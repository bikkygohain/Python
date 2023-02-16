# Basic list operations
#     -   Create a list
#     -   Access items in a list
#     -   Add an item to the list
#     -   Remove an item from the list
#     -   Changes items in the list

#List items are indexed
my_list = ["January", "February", "March"]
print(my_list[2])
my_list.append("April")
print(my_list)
print(my_list[3])
# print(my_list[4])
# Index greater than the no of elements present in the list
# Throws "IndexError: list index out of range"
