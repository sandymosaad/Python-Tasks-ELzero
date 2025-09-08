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