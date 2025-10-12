'''
problem 01:
You are given a Python class representing a game.
Your task is to complete the class definition so that it can store and display information about a game,
including its name, developer, release year, and price in dollars.

You must also create a method that converts the price from US dollars to Egyptian pounds,
using a conversion rate of 1 dollar = 15.6 Egyptian pounds (or the rate used in the code).

Finally, print the game details in the exact required format.
🧩 Requirements:

Define a class named Game.

Add an __init__ method that takes the following parameters:

name

developer

year

price_dollars

Add a method named price_in_pounds() that returns the price in Egyptian pounds.

Create an object of the class with:

Game("Ys", "Falcom", 2010, 50)


Print the information as shown below.
'''

class Game:
    def __init__(self, name,developer,year,price_dollars):
        self.name =name
        self.developer = developer
        self.year = year
        self.price_dollars = price_dollars
    def price_in_pounds (self):
        return self.price_dollars * 15.16
game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"
#------------------------------------Task 1 Done --------------------------------
#---------------------------------------------------------------------------------
'''
problem 02:
complete the contents of a Python class named User so that it produces the expected output shown in the example.

🧩 Requirements:

Create a class called User.

The class should have an __init__ method that takes:

first_name

last_name

age

gender

Add a method named full_details() that:

Displays a greeting using:

"Mr" if the gender is "Male"

"Mrs" if the gender is "Female"

Shows the user’s first name, the first letter of their last name followed by a dot, and

Calculates how many years are left for the user to reach 40 years old.

The message should follow this format:

Hello Mr Osama M. [02] Years To Reach 40
'''
class User:
    def __init__(self,first_name,last_name,age,gender):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.gender = gender

    def full_details(self):
        years_to_40 =40 -self.age
        title = "Mr" if self.gender == "Male" else "Mrs"
        return f" Hello {title} {self.fname} {self.lname[0]}. [{years_to_40:02}] Years To Reach 40 "

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
#------------------------------------Task 2 Done -------------------------------------
#-------------------------------------------------------------------------------------
'''
problem 03:
complete the contents of the class Message so that it produces the expected output shown in the example.

🧩 Requirements:

Create a class named Message.

Inside the class, define a static method called print_message().

The method should return the string:
"Hello From Class Message"
'''
class Message:
    @staticmethod
    def print_message():
        return "Hello From Class Message"

print(Message.print_message())

# Output
# Hello From Class Message
#------------------------------------- Task 3 Done -------------------------------
#---------------------------------------------------------------------------------