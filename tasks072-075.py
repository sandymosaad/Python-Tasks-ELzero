'''
problem 01:
create a function that removes the first and last characters of a string.
# Example: "AEmanS" => "Eman"
use the map function to apply this to a list of names.

'''
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars(friends_map):
    cleaned_list = list(map(lambda name: name[1:-1], friends_map))
    return cleaned_list

ruselt =remove_chars(friends_map)
for name in ruselt:
    print(name)

# another way to solve the problem
def remove_chars_safe(friends_map):
    cleaned = []
    for name in friends_map:
        if isinstance (name,str) and len(name)>= 2:
            cleaned.append(name[1:-1])
        else:
            cleaned.append('')
    return cleaned
#----------------------task 1 done -------------------------------------
#------------------------------------------------------------------------

'''
-----------------------------------
Problem 2:
Filter names ending with 'm'
-----------------------------------
'''

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names(friends_filter):
    # Using filter() to get names ending with 'm'
    names_end_wz_m = list(filter(lambda name: name[-1] == 'm', friends_filter))
    # Alternative way:
    # names_end_with_m = list(filter(lambda name: name.endswith('m'), friends_filter))
    return names_end_wz_m

# Get result
result = get_names(friends_filter)

# Print names that end with 'm'
for name in result:
    print(name)
#-----------------------task 2 done------------------------
#------------------------------------------------------------
'''
problem 03:
make a function to multiply all numbers in a list.
'''
nums = [2, 4, 6, 2]
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

result = multiply(nums)
print(result)

#output:96
#-----------------------task 3 done------------------------
#------------------------------------------------------------



