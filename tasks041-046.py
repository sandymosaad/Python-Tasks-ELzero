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