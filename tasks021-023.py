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
