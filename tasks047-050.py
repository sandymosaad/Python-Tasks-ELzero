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