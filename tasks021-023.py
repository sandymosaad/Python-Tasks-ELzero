# Problem 01:
# Create a list that contains at least 5 of your friends’ names.

# On the first and second lines, print the first friend’s name in two different ways.

# On the third and fourth lines, print the last friend’s name in two different ways.

# Example List:

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama"   => Method One
# "Osama"   => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print(friends[0])
print(friends[-len(friends)])
print(friends[0:1][0])

print(friends[-1])
print(friends[len(friends)-1])
print(friends[-1:][0])

print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:
# From the previous list friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"],

# On the first line, print the names at odd positions (1st, 3rd, 5th …).

# On the second line, print the names at even positions (2nd, 4th …).

# Example Output:

# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0::2])
print(friends[1::2])

print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------
# Problem 03:
# From the list friends,

# On the first line, print the 2nd, 3rd, and 4th names.

# On the second line, print the last name and the one before it.

# Note: The code should work dynamically, even if the number of elements in the list changes.

# Example List:

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print(friends[1:4])
print(friends[-2:])
print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------
# Problem 04:
# Update the last two names in the list friends to "Elzero".

# Example List:

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
friends[-2:]=["Elzero",'Elzero']
print(friends)

print("--------------------task 4 done -----------------------")
#---------------------------------------------------------------
# Problem 05:

# Add a friend’s name to the beginning of the list.

# Then, add another friend’s name to the end of the list.

# Example List:

friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.insert(0, "Nasser")
print(friends)

friends.append('Salem')
print(friends)
print("--------------------task 5 done -----------------------")
#---------------------------------------------------------------
# Problem 06:

# Remove the first two names from the list.

# Then, remove the last name from the list.

# Example List:

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

friends[0:2]=[]

print(friends)

friends[-1:]=[]
print(friends)

# second solition
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Remove first two names
del friends[:2]
print(friends)

# Remove last name
friends.pop()
print(friends)
print("--------------------task 6 done -----------------------")
#---------------------------------------------------------------
