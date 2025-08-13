#task1
#Create three variables that contain your name, age, and country, and make sure their type is String.
myName = "Sandy"
myAge = '24'
myCountry = "Egypt"

#task2
#Print your name, age, and country using the print() function
print(f"'Name: {myName}'")
print(f'"Age:  {myAge}"')
print(f'"Country: {myCountry}"')


#task3
# Create three variables containing your name, age, and country. Then, concatenate these variables with other words to produce the following message exactly:

# "Hello, My Name Is Osama And Iam 38 Years Old and I Live in Egypt."
# Requirements:

# * Use string concatenation (`+`) to combine variables and text.
# * Print the final message.

print("Hello, My Name Is " + myName + " And Iam " + myAge + " Years Old and I Live in " + myCountry + ".")

#task4
#Given the three variables you previously created (name, age, and country), print the type of each variable on a separate line so that the output looks like this:

# <class 'str'>
# <class 'str'>
# <class 'str'>

print(type(myName))
print(type(myAge))
print(type(myCountry))