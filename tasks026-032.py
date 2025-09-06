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
# Problem 03:
# Create a Set containing numbers from 1 to 3.
#print(nums)
# clear the set
#add a & b to the set
#remove c from the set (try to remove it again to show that discard doesn't raise an error if the element is not found)
# print the set after each operation

nums = {1, 2, 3}
print(nums)
nums.clear()
print(nums)
nums.add('a')
nums.add('b')
print(nums)
nums.discard('c')  # discard won't raise an error if 'c' is not found
print(nums)
print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------

# Problem 04:
# create two sets
# check if set_one is subset of set_two
# print the result

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output
#True

print(set_one.issubset(set_two))
print("--------------------task 4 done -----------------------")    
#---------------------------------------------------------------

# Problem 05:
# Create a dictionary to store the following data:
# HTML: 90%
# CSS: 80%
# Python: 30%
# AI: 20%

# Create Dictionary Here
my_dict = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%",
    "AI": "20%"
}

# Needed Output

# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"
# "AI Progress Is 20%"
# don't Loop for the output

print(f"HTML Progress Is {my_dict['HTML']}")
print(f"CSS Progress Is {my_dict['CSS']}")  
print(f"Python Progress Is {my_dict['Python']}")
print(f"AI Progress Is {my_dict['AI']}")
print("--------------------task 5 done -----------------------")
#---------------------------------------------------------------

