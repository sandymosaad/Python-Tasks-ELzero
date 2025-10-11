'''
problem 01:

You are given the following code that takes an input from the user:

```python
NUM = input("Add Your Number ")
# Your Code Here
```

You need to complete the code so that it handles different user inputs using **Exceptions** — not regular print statements.

#### ✅ **Requirements:**

1. If the user enters **more than one character**, raise this error:

    ```
    IndexError: Only One Character Allowed
    ```

2. If the user enters a **number greater than 0**, show the number using this format:

    ```
    ####################
    The Number Is 9
    ####################
    ```

3. If the user enters **0**, raise this error:

    ```
    ValueError: Number Must Be Larger Than 0
    ```

4. If the user enters **any English letter** (uppercase or lowercase), raise this error:

    ```
    Exception: Only Numbers Allowed
    ```

> ⚠️ All the displayed messages must be **Exceptions and Errors**, not printed messages.


'''


NUM = input("Add Your Number ")

if len(NUM) > 1:
    raise IndexError("Only One Character Allowed")

elif NUM.isalpha():
    raise Exception("Only Numbers Allowed")

elif NUM == '0':
    raise ValueError("Number Must Be Larger Than 0")

elif NUM.isdigit():
    print("####################")
    print(f"The Number Is {NUM}")
    print("####################")

else:
    raise Exception("Invalid Input")



#------------------Task 01 Done -------------
#--------------------------------------------
#---------------------------------------------

'''
problem 02:
Handle user input with try, except, else
'''

# LETTER = input("Add Letter From A to Z: ")
LETTER='S'

try:
    # Check if user entered more than one character
    if len(LETTER) != 1:
        raise ValueError("You Must Write One Character Only")

    # Check if input is not a capital letter A–Z
    elif not LETTER.isalpha() or not LETTER.isupper():
        raise Exception("The Letter Not In A - Z")

except ValueError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print(f"You Typed {LETTER}")

#------------------Task 02 Done --------------
#---------------------------------------------

'''
problem 03:
Use Type Hinting in the function to specify parameter and return types.
'''

def calculate(num1: int, num2: int) -> int:
    """Return the sum of two numbers."""
    return num1 + num2

# Test the function
print(calculate(20, 30))  # Output => 50

#------------------Task 03 Done ----------------
#-----------------------------------------------