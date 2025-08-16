#Problem 01:
#Print all the main types of numbers in Python, each on a separate line.

# Integer
print(10)
print(type(10))

# Float
print(10.5)
print(type(10.5))

# Complex
print(1 + 2j)
print(type(1+ 2j))

print ("-----------------task 1 done ---------------")
#--------------------------------------------------------

# Problem 02:
# Given the complex number 1+2j, print its imaginary part on the first line and its real part on the second line.

# Example:

num = 1 + 2j

# Print Imaginary Part Here
# Print Real Part Here

# Needed Output:

# 2.0
# 1.0
print(num.imag)
print(num.real)

print ("-----------------task 2 done ---------------")
#--------------------------------------------------------------

# Problem 03:
# Convert the number 10 into a floating-point number with 10 decimal places after the decimal point.

# Example:

num = 10

# Needed Output
# 10.0000000000

print(f"{num:.10f}")
print ("-----------------task 3 done ---------------")
#--------------------------------------------------------------

# Problem 04:
# Convert the number 159.650 into an integer.

# On the first line, print the converted number.

# On the second line, print its type to confirm it is an integer.

# Example:

num = 159.650

# Needed Output
# 159
# <class 'int'>

num_int = int(num)
print(num_int)
print(type(num_int))

print ("-----------------task 4 done ---------------")
#--------------------------------------------------------------
# Problem 05:
# Replace the question mark ? with the correct arithmetic operator so that each equation becomes true.

# Examples:

# 100 ? 115 = -15    
# 50 ? 30  = 1500     
# 21 ? 4   = 1        
# 110 ? 11 = 10       
# 97 ? 20  = 4       

print(100 - 115)
print(50 * 30 )
print(21 % 4)
print(110/11)
print(97//20)