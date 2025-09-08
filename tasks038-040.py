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