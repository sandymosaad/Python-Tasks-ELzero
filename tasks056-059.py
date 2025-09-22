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