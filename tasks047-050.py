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