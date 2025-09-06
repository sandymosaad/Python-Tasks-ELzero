# Problem 01:
# Create a Tuple with only one element (your name) without using parentheses ().

# On the first line, print the single element in the tuple.

# On the second line, print the type to make sure it is a tuple.

# Needed Output

# Osama
# <class 'tuple'>


name_tuple = "Osama",
print(name_tuple[0])
print(type(name_tuple))

print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:

# Create a Tuple with 3 of your friends’ names, the first one must be "Osama".

# Use what you learned to change the first name from "Osama" to "Elzero".

# Print the updated tuple.

# Print the type to confirm it is a tuple.

# Print the number of elements inside the tuple.

# Needed Output:

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements

# Original tuple
friends = ("Osama", "Ahmed", "Sayed")

# Update first element to "Elzero" by creating a new tuple and concatenating it with the rest
updated_friends = ("Elzero",) + friends[1:]
print(updated_friends)
print(type(updated_friends))
print(f"{len(updated_friends)} Elements")

# Tuples are immutable → convert to list → modify → back to tuple
friends = list(friends)
friends[0] = "Elzero"
friends = tuple(friends)

# Print updated tuple
print(friends)

# Print type
print(type(friends))

# Print number of elements
print(f"{len(friends)} Elements")

print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------