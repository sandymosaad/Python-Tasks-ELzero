
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