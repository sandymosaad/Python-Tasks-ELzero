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
print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:
# Create a set containing numbers from 1 to 3.
# Create another set containing letters from "A" to "C".
# Concatenate them into a new set.
# Print the new set.
# Print the new set again using a different method.
nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

# Concatenate sets in three different ways

# 1. use union
nums_and_letters1 = nums.union(letters)
print(nums_and_letters1)

# 2. use update (modifies nums itself)
nums2 = {1, 2, 3}  # redefine nums so it doesn't change for the following examples
nums2.update(letters)
print(nums2)

# 3. use | (or)
nums_and_letters3 = nums | letters
print(nums_and_letters3)
print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------
