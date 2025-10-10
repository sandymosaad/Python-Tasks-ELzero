
'''
problem 01:
Write the correct code inside the loop only to produce the output shown below.
Do not modify any existing lines in the code.
'''
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    my_data.extend(data)

final_string = ''.join(my_data)
print(final_string)  # Elzero
#---------------------task 01 done -------------
#-----------------------------------------------
'''
problem 02:
Write the correct code inside the loop to get the output "Elzero"
Do not modify any existing code
'''

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # Write Your Code Here
    if isinstance(item1, str):
        my_data.append(item1)

final_string = ''.join(my_data)
print(final_string)  # Elzero
#-----------------task 2 done -------------
#------------------------------------------