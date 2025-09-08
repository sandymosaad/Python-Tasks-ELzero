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

# Problem 04:
# Create a variable named num_one with value 10
# Create a variable named num_two with value 20
# Store the sum of the two variables in a new variable named result and print it in the first line
# In the second line, print the result raised to the exponent 3
# In the third line, print the remainder of dividing the previous result by 26000
# In the fourth line, print the result of dividing the previous number by 5 (should be float)
# In the fifth line, print the type after converting it to string to make sure it's a string

num_one = 10
num_two = 20
# Step 1: Sum
result = num_one + num_two
print(result)  # 30
# Step 2: Exponent 3
exp_result = result ** 3
print(exp_result)  # 27000
# Step 3: Modulus 26000
mod_result = exp_result % 26000
print(mod_result)  # 1000
# Step 4: Divide by 5 (float)
div_result = mod_result / 5
print(div_result)  # 200.0
# Step 5: Convert to string and print type
str_result = str(div_result)
print(type(str_result))  # <class 'str'>

print("--------------------task 4 done -----------------------")
#---------------------------------------------------------------