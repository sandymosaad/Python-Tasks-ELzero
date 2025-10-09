'''
problem 01:
Use the yield keyword with what you’ve learned to reverse a string.
After that, make sure the loop works successfully and outputs the required result.

'''
def reverse_string(my_string):
    for char in my_string[::-1]:
        yield char
# Reverse The String
for c in reverse_string("Elzero"):
  print(c)

print('----------------------')
# another solution
def reverse_string(my_string):
    for char in reversed(my_string):
        yield char

for c in reverse_string("Elzero"):
  print(c)
#--------------------task 1 done ----------------
#-------------------------------------------------

'''
problem 02:
Create a Decorator Function that does the following:

Prints a message before the main function:
"Sugar Added From Decorators"

Prints a separator made of # symbols after the main function.

Then, use this decorator with the existing functions.
Expected Output:

Sugar Added From Decorators
Tea Created
####################
Sugar Added From Decorators
Coffe Created
####################
'''

# Create Your Decorator Here
def my_decorator(func):
    def wrapper():
        print("Sugar Added From Decorators")
        func()
        print("#" * 20)
    return wrapper


@my_decorator
def make_tea():
  print("Tea Created")

@my_decorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()
#-------------------------task 2 done ---------------------
#-----------------------------------------------------------
