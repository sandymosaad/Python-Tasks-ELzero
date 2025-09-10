# Problem 01:
# Create a variable named num that takes a number input from the user.
# If the number is 0, print "Number 0 Is Not Larger Than 0".
# Otherwise, print the number and all the numbers that come before it, except the last number.
# Make sure to skip the number 6 if it comes in the sequence.
# Finally, print a message that indicates how many numbers were printed successfully.

num = int(input("Enter A Number: ").strip())
if num == 0:
    print("Number 0 Is Not Larger Than 0")
else:
    num_count = num    
    while num_count >0:
        num_count -= 1
        if num_count != 6 and num_count != 0:
            print(num_count)
    print(f"{num-2} Numbers Printed Successfully.")

print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:
# Create a list with five friends' names, at least two in all lowercase and the rest with the first letter capitalized.
# Use a while loop to print all names, ignoring those that start with a lowercase letter.
# Print the number of ignored names programmatically.

friends = ["osama", "ahmed", "Sayed", "Ali", "Mahmoud"]
index = 0
ignored_count = 0
while index < len(friends):
    name = friends[index]
    if name[0].islower():
        ignored_count += 1
    else:
        print(name)
    index += 1
print(f"Friends Printed And Ignored Names Count Is {ignored_count}")
print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------
# Problem 03:
# Create a list named skills that contains the following programming skills: "HTML", "CSS", "JavaScript", "PHP", "Python".
# Use a while loop to print each skill in the list one by one.

# Needed Output
# "HTML"
# "CSS"
# "JavaScript"
# "PHP"
# "Python"


# Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:

  # Type The Code Here in One Line
    print(skills.pop(0))

print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------
# Problem 04:
# Create a list named my_friends that contains at least 4 friends' names.
# Use a while loop to allow the user to add more friends' names to the list until it contains 4 names.
# Make sure the first letter of each name is capitalized and the rest are small.
# Print a message for each added name.
# If the name is all uppercase, print a message that the name can't be all uppercase and
# don't add it to the list.
# If the name is all lowercase, capitalize the first letter and add it to the list,
# and print a message that the name was added and capitalized.
# If the name is in title case (first letter capitalized), add it to the list
# and print a message that the name was added.
# If the name is mixed case (some letters uppercase and some lowercase),
# capitalize the first letter and add it to the list,
# and print a message that the name was added and capitalized.

my_friends = []
max_friends = 4

while len(my_friends) < max_friends:
    new_friend = input("Enter Your Friend Name: ").strip()
    if new_friend.isupper():
        print("Friend Name Can't Be All Uppercase")
        continue
    elif new_friend.islower():
        new_friend = new_friend.capitalize()
        my_friends.append(new_friend)
        print(f"{new_friend} Added and Capitalized first letter")
    elif new_friend.istitle():
        my_friends.append(new_friend)
        print(f"{new_friend} Added")
    else:
        new_friend = new_friend.capitalize()
        my_friends.append(new_friend)
        print(f"{new_friend} Added and Capitalized first letter")
    places_left = max_friends - len(my_friends)
    if places_left > 0:
        print(f"{places_left} Places Left")
print(my_friends)
print("--------------------task 4 done -----------------------")
#---------------------------------------------------------------