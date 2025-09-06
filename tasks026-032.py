# Problem 01:
# Create a list with numbers that contains at least one duplicate element.
# Remove the duplicates and print the list.
# Then remove the last element from the list and print the list again.
# Example List:
my_list = [1, 2, 3, 3, 4, 5, 1]

# Needed Output:
# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4

my_list = list(set(my_list))
print(my_list)
print(type(my_list))

my_list.pop()
print(my_list)