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




