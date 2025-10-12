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