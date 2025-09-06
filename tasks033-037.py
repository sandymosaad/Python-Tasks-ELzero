# Problem 01:

# in the first 4 lines, using Bool Method, print 4 different data types that result in True
# in lines 5 to 8, using Bool Method, print 4 different data types that result in False

# Needed Output
# True
# True
# True
# True
# False
# False
# False
# False

print(bool(1))
print(bool("Hello"))
print(bool([1, 2, 3]))
print(bool({1, 2, 3}))  
print(bool(0))
print(bool("")) 
print(bool([]))
print(bool({}))
print(bool(None))

print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:
# create three variables with names of any programming skills you have, and their values should be your proficiency percentage in those skills, all above 50%.
# In a single line, using Boolean Operators, check if your proficiency in all skills is greater
# than 50%. Do not use If Condition here, and the result should be True.
html = 80
css = 60
javascript = 70

# Needed Output
#True
print(html > 50 and css > 50 and javascript > 50)
print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------
# Problem 03:
# create three variables num_one, num_two, and num with values 10, 20, and 20 respectively.
# On the first line, print the result of checking if num is greater than one of the other two variables but not both.
# On the second line, print the result of checking if num is greater than both other variables.
# Needed Output
#True
#False

num_one = 10
num_two = 20
num = 20

print(num > num_one or num < num_two)   # True
print(num > num_one and num > num_two)  # False
print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------
