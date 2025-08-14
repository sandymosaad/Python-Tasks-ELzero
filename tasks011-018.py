# Problem1:
# Create three variables containing your name, age, and country. Then, concatenate these variables with the following words and symbols to produce the exact message below. Make sure to include all quotes, backslashes, and spaces exactly as shown:


# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt"
# Requirements:

# Use string concatenation (+) to combine variables and text.

# Print the final message exactly as shown, preserving all symbols and formatting.

myName = "Sandy"
myAge = '24'
myCountry = "Egypt"

print("\"Hello '"+myName+"', How you doing \\ \"\"\" Your age is \""+myAge+"\"\" + and your country is : "+myCountry)

#--------------------------------------------------------------------------------
# Problem 02:
# Print the same message from the previous task, but split it across multiple lines. Make sure the output matches exactly as shown below, preserving all quotes, backslashes, plus signs, and spacing:

# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt"
# Requirements:

# Use string concatenation (+) or multi-line strings to split the message.

# Print the final message exactly as shown.

print("\"Hello '"+myName+"', How you doing \\ \n \"\"\" Your age is \""+myAge+"\"\" +\n and your country is : "+myCountry)

#--------------------------------------------------------------------------------
# Problem 03:
# Create a variable name containing the value "Elzero". Then, using Indexing and Slicing, extract the following letters:

# The second letter on the first line

# The third letter on the second line

# The last letter on the third line

# Make sure to extract the letters dynamically, so that the code still works if the value of name changes.

# Example:

# name = 'Elzero'

# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
#Hint: Use name[index] or name[start:end] to get the letters.
name = "Elzero"
print(f" Second Letter Is : \"{name[1]}\"")
print(f" Third  Letter Is : \"{name[2]}\"") 
print(f" Last  Letter Is : \"{name[-1]}\"") 

print(f" Second Letter Is : \"{name[1:2]}\"")
print(f" Third Letter Is : \"{name[2:3]}\"")
print(f" Last  Letter Is : \"{name[-1:]}\"")

#--------------------------------------------------------------------------------
# Problem 04:
# Using the variable name = "Elzero" from the previous task, extract more than one letter using Indexing and Slicing. Your code should produce the following output exactly:

# name = 'Elzero'

# Needed Output
# "lze"
# "Ezr"
# "rzE"
#Requirements:

# Use slicing (name[start:end]) and indexing to get the letters.

# Make sure the code works dynamically if the value of name changes.
print(f"\"{name[1:4]}\"")
print((f"\"{name[::2]}\""))
print(f"\"{name[-2::-2]}\"")

#--------------------------------------------------------------------------------
# Problem 05:
# Given the variable name = "#@#@Elzero#@#@", remove all extra symbols or characters surrounding the word so that only the word itself remains.
# Example:
# name = "#@#@Elzero#@#@"

# Needed Output
# Elzero

#Hint: Use strip() method to remove characters from the string.
name = "#@#@Elzero#@#@"
print(name.strip('#@'))
#--------------------------------------------------------------------------------
# Problem 06:
# Create a variable containing any number you want as a string. Then, add leading zeros so that the number always has a width of 4 digits.

# Example:

# num = "9"
# num = "15"
# num = "130"
# num = "950"
# num = "1500"

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

#--------------------------------------------------------------------------------
# Problem 07:
# Add @ symbols before any string you are given, so that the total length does not exceed 20 characters.

# Example:
name_one = "Osama"
name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

print(name_one.rjust(20, '@'))
print(name_two.rjust(20, '@'))
#--------------------------------------------------------------------------------
# Problem 08:
# Given the variables name_one and name_two, swap the case of each letter:

# Convert uppercase letters to lowercase

# Convert lowercase letters to uppercase

# Example:

name_one = "OSamA"
name_two = "osaMA"

# Needed Output
# osAMa
# OSAma

print(name_one.swapcase())
print(name_two.swapcase())
#--------------------------------------------------------------------------------
# Problem 09:
# Given the string msg, count how many times the word "Love" appears in it.

# Example:
msg = "I Love Python And Although Love Elzero Web School"

# Needed Output
# 2

print(msg.count("Love"))
#--------------------------------------------------------------------------------
# Problem 10:
# Given the string name = "Elzero", print the position (index) of the letter z in the word.

# Example:
# name = "Elzero"

# Needed Output
# 2

print(name.index("z"))
#--------------------------------------------------------------------------------
# Problem 11:
# Given the string msg = "I <3 Python And Although <3 Elzero Web School", replace the first occurrence of the substring "<3" with the word "Love" only once.

# Example:
# msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although <3 Elzero Web School

print(msg.replace("<3", "Love", 1))
#--------------------------------------------------------------------------------
# Problem 12:
#Given the string msg = "I <3 Python And Although <3 Elzero Web School", replace all occurrences of the substring "<3" with the word "Love".
# Example:
# msg = "I <3 Python And Although <3 Elzero Web School"

# Needed Output
# I Love Python And Although 3< Elzero Web School

print(msg.replace("<3", "Love"))
#--------------------------------------------------------------------------------
# Problem 13:
# Create three variables containing your name, age, and country. Make sure that age is an integer, not a string. Then, print the following message using the new f-string formatting method (f""):

name = "Osama"
age = 38
country = "Egypt"

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt

print(f"My name is {name}, and my age is {age}, and my country is {country}")