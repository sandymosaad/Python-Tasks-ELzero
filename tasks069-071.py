'''
problem: 01
# Without running the code below, try to determine what will be the output
# After you write your prediction, run the code to see if you were correct
# add comments to explain how you reached your conclusion
'''

# tuple of values
values = (0, 1, 2)

'''
check if any value is true
'''
if any(values):

    my_var = 0

# list of mixed values 
my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

''' check if all values are true for the first 4 values,or first 6 values, or all values '''
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")
# Output
# Good

#------------------------------task 1 done -----------------------
#---------------------------------------------------------------
'''
problem: 02
what is the value of v that makes the output of the code below equal to 820
v = ??

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820
'''

v = 1
while True:
    my_range = list(range(v))
    result = sum(my_range, v) + pow(v, v, v)
    if result == 820:
        print(f"v = {v}, result = {result}")
        break
    v += 1
# Another way to find v using a generator expression
# This will find the first v in the range 1 to 99 that satisfies the condition
# and print it directly without a loop


v = next(v for v in range(1, 100) if sum(range(v), v) + pow(v, v, v) == 820)
print(v)


#------------------------------task 2 done -----------------------
#---------------------------------------------------------------
'''
Problem 03:
What is the output of the code below
n = ??

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good
'''
n=1
while True:
    l = list(range(n))
    if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
        print(f"n = {n}, Output => Good")
        break
    n += 1
# Another way to find n using a generator expression
n = next(n for n in range(1, 100) if round(sum(range(n)) / n) == max(0, 3, 10, 2, -100, -23, 9))
print(f"n = {n}, Output => Good")   
#------------------------------task 3 done -----------------------
#---------------------------------------------------------------
'''
Problem 04:
explain the my_all and my_any functions in your own words
# my_all function checks if all elements in the given iterable are truthy (i.e., evaluate to True).
# It returns True if all elements are truthy, and False if any element is falsy (i.e., evaluates to False).
# If the iterable is empty, it returns True by definition, as there are no falsy elements.
# my_any function checks if any element in the given iterable is truthy.    
# It returns True if at least one element is truthy, and False if all elements are falsy.
# If the iterable is empty, it returns False by definition, as there are no truthy elements.
# Both functions iterate through the elements of the iterable and use conditional checks to determine their return values.
'''

def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
# Tests
print(my_all([1, 2, 3]))          # True
print(my_all([1, 2, 3, 0]))       # False
print(my_all([]))                  # True

def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False
# Tests
print(my_any([0, "", None]))      # False
print(my_any([0, "", None, 1]))   # True

def my_min(iterable):
    min_value = None
    for element in iterable:
        if min_value is None or element < min_value:
            min_value = element
    return min_value
# Tests
print(my_min([3, 1, 4, 1, 5, 9]))  # 1
print(my_min([-3, -1, -4, -1, -5, -9]))  # -9
print(my_min([42]))                 # 42
print(my_min([]))                   # None

def my_max(iterable):
    max_value = None
    for element in iterable:
        if max_value is None or element > max_value:
            max_value = element
    return max_value
# Tests
print(my_max([3, 1, 4, 1, 5, 9]))  # 9
print(my_max([-3, -1, -4, -1, -5, -9]))  # -1
print(my_max([42]))                 # 42
print(my_max([]))                   # None

#------------------------------task 4 done -----------------------
