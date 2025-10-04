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

'''check if all values are true for the first 4 values,or first 6 values, or all values '''
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")
# Output
# Good