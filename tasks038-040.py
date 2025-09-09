# Problem 01:

# Create a variable named name that takes the user's input for their name.
# Make sure to remove any spaces before and after the name.
# Make sure the name is capitalized (first letter capital, rest small).
# Print the name with a welcome message.
# Input
#"     osAmA   "

# Needed Output
#"Hello Osama, Happy To See You Here."

input_Name = input("Enter Your Name: ").strip().capitalize()
print(f"Hello {input_Name}, Happy to see you here")
print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:
#Create a variable named age that takes the user's input for their age.
# Make sure the input is converted to an integer, not a string.
# If the age is less than 16, print a message that the site contains articles not suitable for under 16.
# If the age is 16 or older, print a welcome message with the age and that the site is suitable.

age = int(input("How Old Are You? ").strip())
if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
elif 16 <= age:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You") # If Age Is 16+

print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------
# Problem 03:
# Problem:
# Create two variables named first_name and second_name that take the user's input for their first and second names.
# Make sure to remove any spaces before and after each name.
# Make sure the first letter of each name is capitalized and the rest are small.
# Print a welcome message that includes the first name and the first letter of the second name only.

fname =input("Enter Your First Name: ").strip().capitalize()
sname =input("Enter Your Second Name: ").strip().capitalize()
print(f"Hello {fname} {sname[0]} , How Are You?")

print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------
# Problem 04:
# Create a variable named email that takes the user's input for their email address.
# Make sure to remove any spaces before and after the email.
# Make sure all letters are lower case.
# Print a message in the first line with the person's name only (before the @), with the first letter capitalized.
# Print a message in the second line with the site name only (between @ and the dot).
# Print a message in the third line with the top level domain (after the dot).

email = input("Enter Your Email: ").strip().lower()
print(f"Full Email: {email}")
print(f'Email Username: {email[:email.index("@")].capitalize()}')
print(f"Website Name: {email[email.index("@")+1:email.index(".")]}")
print(f"Email Extension: {email[email.index(".")+1:]}")

print("--------------------task 4 done -----------------------")

#---------------------------------------------------------------







################## tasks041-046 ##################
# Problem 01:
# Create a variable named num1 and assign it the value of the first number taken from the user.
# Create a variable named num2 and assign it the value of the second number taken from the user.
# Create a variable named operation and assign it the value of the operation taken from the user.
# If the operation is one of the following: +, -, *, /, %, //, **, print the result of the operation.
# Otherwise, print an error message.

# num1= int(input("Enter First Number: ").strip())
# num2=int(input("Enter Second Number: ").strip())
# operation=input("Enter The Operation (+ - * / % // **): ").strip()
# if operation == "+":
#     print(f"{num1} {operation} {num2} = {num1 + num2}")
# elif operation == "-":
#     print(f"{num1} {operation} {num2} = {num1 - num2}")
# elif operation == "*":
#     print(f"{num1} {operation} {num2} = {num1 * num2}")
# elif operation == "/":
#     print(f"{num1} {operation} {num2} = {num1 / num2}")
# elif operation == "%":
#     print(f"{num1} {operation} {num2} = {num1 % num2}")
# elif operation == "//":
#     print(f"{num1} {operation} {num2} = {num1 // num2}")
# elif operation == "**":
#     print(f"{num1} {operation} {num2} = {num1 ** num2}")
# else:
#     print("Invalid Operation")

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

# age = int(input("How Old Are You? ").strip())
# if age > 10 and age < 100:
#     months = age * 12
#     weeks = age * 52
#     days = age * 365
#     hours = days * 24
#     minutes = hours * 60
#     seconds = minutes * 60
#     print(f"Your Age In Months Is: {months}")
#     print(f"Your Age In Weeks Is: {weeks}")
#     print(f"Your Age In Days Is: {days}")
#     print(f"Your Age In Hours Is: {hours}")
#     print(f"Your Age In Minutes Is: {minutes}")
#     print(f"Your Age In Seconds Is: {seconds}")
# else:
#     print("Your Age Is Not Valid")
print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------
# Problem 04:
# Create a variable named country that takes the user's input for their country.
# Make sure to remove any spaces before and after the country name.
# Make sure the first letter of each word in the country name is capitalized and the rest are small.
# Create a list of countries that are eligible for a discount: "Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England".
# Create a variable named price and assign it the value of 100.
# Create a variable named discount and assign it the value of 30.
# If the country is in the list of eligible countries, print a message with the country name and the price after applying the discount.
# If the country is not in the list, print a message that the country is not eligible for the discount and the full price.

# country = input("Input Your Country").strip().capitalize()
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# price = 100
# discount = 30
# if country in countries:
#     discounted_price = price - (price * discount / 100)
#     print(f"Your Country Is {country}, Your Price After Discount Is {discounted_price}")
# else:
#     print(f"Your Country Is Not Eligible For Discount, Your Price Is {price}")
print("--------------------task 4 done -----------------------")
#---------------------------------------------------------------
################## tasks047-050 ##################
# Problem 01:
# Create a variable named num that takes a number input from the user.
# If the number is 0, print "Number 0 Is Not Larger Than 0".
# Otherwise, print the number and all the numbers that come before it, except the last number.
# Make sure to skip the number 6 if it comes in the sequence.
# Finally, print a message that indicates how many numbers were printed successfully.

# num = int(input("Enter A Number: ").strip())
# if num == 0:
#     print("Number 0 Is Not Larger Than 0")
# else:
#     num_count = num    
#     while num_count >0:
#         num_count -= 1
#         if num_count != 6 and num_count != 0:
#             print(num_count)
#     print(f"{num-2} Numbers Printed Successfully.")

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

# while len(my_friends) < max_friends:
#     new_friend = input("Enter Your Friend Name: ").strip()
#     if new_friend.isupper():
#         print("Friend Name Can't Be All Uppercase")
#         continue
#     elif new_friend.islower():
#         new_friend = new_friend.capitalize()
#         my_friends.append(new_friend)
#         print(f"{new_friend} Added and Capitalized first letter")
#     elif new_friend.istitle():
#         my_friends.append(new_friend)
#         print(f"{new_friend} Added")
#     else:
#         new_friend = new_friend.capitalize()
#         my_friends.append(new_friend)
#         print(f"{new_friend} Added and Capitalized first letter")
#     places_left = max_friends - len(my_friends)
#     if places_left > 0:
#         print(f"{places_left} Places Left")
# print(my_friends)
print("--------------------task 4 done -----------------------")
#---------------------------------------------------------------
################### tasks051-055 ##################

# Problem 01:
# Create a list named my_nums that contains the following numbers:
# 15, 81, 5, 17, 20, 21, 13, 30, 65, 10, 7, 9.
# Sort the list in descending order.
# Use a for loop to print all the numbers that are multiples of 5.
# Finally, print a message that all numbers have been printed successfully. 
my_nums = [15, 81, 5, 17, 20, 21, 13, 30, 65, 10, 7, 9]
my_nums.sort(reverse=True)

count = 1
for num in my_nums:
    if num % 5 == 0:
        print(f"{count} => {num}")
        count += 1
print("All Numbers Printed Successfully.")
print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:
# Use a for loop to print all the numbers from 1 to 20.
# Skip the numbers 6, 8, and 12.
# Use the zfill() method to print the numbers with leading zeros.

for num in range(1, 21):
    if num == 6 or num == 8 or num == 12:
        continue
    #print(num, type(num))
    print(str(num).zfill(2))
print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------
# Problem 03:
# Create a dictionary named my_ranks that contains your ranks in the following subjects:
# Math: A
# Science: B
# Drawing: A
# Sports: C
# Calculate and print the total score based on the following rules:
# Rank A: 100 points
# Rank B: 80 points
# Rank C: 40 points

# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
# Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"


total_score = 0
for subject, rank in my_ranks.items():
    if rank == 'A':
        print(f"Your Rank in {subject} Is {rank}, And This Equal 100 Points.")
        total_score += 100
    elif rank == 'B':
        print(f"Your Rank in {subject} Is {rank}, And This Equal 80 Points.")
        total_score += 80
    elif rank == 'C':
        print(f"Your Rank in {subject} Is {rank}, And This Equal 40 Points.")
        total_score += 40
print(f"Total Score Is {total_score} Points.")

print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------
# Problem 04:
# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
# for student, subjects in students.items():
#     print("------------------------------")
#     print(f"-- Student Name: {student}")
#     print("------------------------------")
#     total_score = 0
#     for subject, rank in subjects.items():
#         if rank == 'A':
#             print(f'{subject} => {rank} => 100 Points')
#             total_score += 100
#         elif rank == 'B':
#             print(f'{subject} => {rank} => 80 Points')
#             total_score += 80
#         elif rank == 'C':
#             print(f'{subject} => {rank} => 40 Points')
#             total_score += 40
#         elif rank == 'D':
#             print(f'{subject} => {rank} => 20 Points')
#             total_score += 20
#     print(f"Total Score For {student} Is {total_score} Points.")

#another solution
for student in students:
    print("------------------------------")
    print(f"-- Student Name: {student}")
    print("------------------------------")
    total_score = 0
    for subject in students[student]:
        rank = students[student][subject]
        if rank == 'A':
            print(f'{subject} => {rank} => 100 Points')
            total_score += 100
        elif rank == 'B':
            print(f'{subject} => {rank} => 80 Points')
            total_score += 80
        elif rank == 'C':
            print(f'{subject} => {rank} => 40 Points')
            total_score += 40
        elif rank == 'D':
            print(f'{subject} => {rank} => 20 Points')
            total_score += 20
    print(f"Total Score For {student} Is {total_score} Points.")
print("--------------------task 4 done -----------------------")
#---------------------------------------------------------------