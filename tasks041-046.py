# Problem 01:
# Create a variable named num1 and assign it the value of the first number taken from the user.
# Create a variable named num2 and assign it the value of the second number taken from the user.
# Create a variable named operation and assign it the value of the operation taken from the user.
# If the operation is one of the following: +, -, *, /, %, //, **, print the result of the operation.
# Otherwise, print an error message.

num1= int(input("Enter First Number: ").strip())
num2=int(input("Enter Second Number: ").strip())
operation=input("Enter The Operation (+ - * / % // **): ").strip()
if operation == "+":
    print(f"{num1} {operation} {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} {operation} {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} {operation} {num2} = {num1 * num2}")
elif operation == "/":
    print(f"{num1} {operation} {num2} = {num1 / num2}")
elif operation == "%":
    print(f"{num1} {operation} {num2} = {num1 % num2}")
elif operation == "//":
    print(f"{num1} {operation} {num2} = {num1 // num2}")
elif operation == "**":
    print(f"{num1} {operation} {num2} = {num1 ** num2}")
else:
    print("Invalid Operation")

print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:
# Create a variable named age and assign it your age.
# Using a single line of code, print "App Is Suitable For You" if the age is 16 or older.
# Otherwise, print "App Is Not Suitable For You".   


age = 13
print('App Is Suitable For You' if age >= 16 else 'App Is Not Suitable For You')

print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------

# Problem 03:
# Create a variable named age that takes the user's input for their age.
# Make sure the input is converted to an integer, not a string.
# Make sure to remove any spaces before and after the age.
# If the age is between 10 and 100, print the following message:

# Your Age In Months Is: x
# Your Age In Weeks Is: x   
# Your Age In Days Is: x
# Your Age In Hours Is: x
# Your Age In Minutes Is: x
# Your Age In Seconds Is: x

# If the age is not between 10 and 100, print a message that the age is not valid.  

age = int(input("How Old Are You? ").strip())
if age > 10 and age < 100:
    months = age * 12
    weeks = age * 52
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print(f"Your Age In Months Is: {months}")
    print(f"Your Age In Weeks Is: {weeks}")
    print(f"Your Age In Days Is: {days}")
    print(f"Your Age In Hours Is: {hours}")
    print(f"Your Age In Minutes Is: {minutes}")
    print(f"Your Age In Seconds Is: {seconds}")
else:
    print("Your Age Is Not Valid")
print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------