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


