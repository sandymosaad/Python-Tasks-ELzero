"""
Problem 1:
Create a calculate function that performs arithmetic operations
- Function accepts three parameters (first number, second number, operation type)
- Available operations are: add, subtract, multiply
- Operation type can be written in any case (add, ADD, aDd)
- User can write first letter only (s or S for subtract)
- If no operation is provided, default to addition
"""

def calculate(num1, num2, operator=None):
    # Convert operator to lowercase if it exists
    if operator:
        operator = operator.lower()
     
    if operator is None:
        return num1 + num2
    elif operator == "add" or operator == "a":
        return num1 + num2
    elif operator == "subtract" or operator == "s":
        return num1 - num2
    elif operator == "multiply" or operator == "m":
        return num1 * num2
    elif operator == "divide" or operator == "d":
        return num1 / num2
    else:
        return "Invalid Operator"

# Test cases
print(calculate(10, 20))         # 30
print(calculate(10, 20, "ADD"))  # 30
print(calculate(10, 20, "s"))    # -10
print(calculate(10, 20, "M"))    # 200
print(calculate(10, 20, "x"))    # Invalid Operator

print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
"""
Problem 2:
Create an addition function that accepts any number of parameters
- Function should return the sum of the parameters
- If the function encounters the number 10, it should skip it and not add it to the total
- If the function encounters the number 5, it should subtract it from the total
"""
def addition(*nums):
    total = 0
    for num in nums:
        if num == 10:
            continue
        elif num == 5:
            total -= 5
        else:
            total += num
    return total
# Test cases
print(addition(10, 20, 30))        # 50
print(addition(10, 20, 30, 40))    # 100
print(addition(10, 20, 30, 40, 50))# 150
print(addition(10, 5, 20, 30))     # 45
print(addition(10, 5, 20, 30, 5))  # 40

print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------