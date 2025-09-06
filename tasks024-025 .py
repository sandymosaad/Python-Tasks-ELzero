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
# Problem 03:

# Create a tuple containing numbers from 1 to 3.

# Create another tuple containing letters from "A" to "C".

# Concatenate them into a new tuple.

# Print the new tuple.

# Print the number of elements inside the new tuple.

# Needed Output:

# (1, 2, 3, 'A', 'B', 'C')
# 6 Elements
# Tuples

nums = (1, 2, 3)
letters = ("A", "B", "C")

# Concatenate tuples
nums_and_letters_one = nums + letters

# Print the new tuple
print(nums_and_letters_one)

# Print the number of elements
print(f"{len(nums_and_letters_one)} Elements")

# Print type
print(type(nums_and_letters_one))

print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------
# Problem 04:
# Create a tuple containing numbers from 1 to 4.
# Unpack the tuple into 3 variables, ignoring the 3rd value.
# Print the 3 variables.
# Print the type of the tuple.

# Needed Output:

# 1
# 2
# 4
# <class 'tuple'>   

my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple  # Using underscore for the value we want to ignore
print(a)
print(b)
print(c)
print(type(my_tuple))
print("--------------------task 4 done -----------------------")
#---------------------------------------------------------------

