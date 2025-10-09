'''
problem 01:
Generate random numbers (normal, even, odd) and print module methods
'''
import random

print(f'Random Number Between 10 And 50 =>{random.randint(10,50)} ')

print(f'Random Even Number Between 2 And 10 => {random.randrange(2, 11, 2)} ')

print(f"Random Odd Number Between 1 And 9 => {random.randrange(1,10,2)} ")

print("\n# Module Methods Content Here")
print(dir(random))
#------------------------task 1 done-------------------------
#----------------------------------------------------------
'''
problem 02:
Create folder named python if not exists and create 2 files main.py and my_mod.py
create function in main and imort in my_mode and print the result
'''
import os
current_path = os.getcwd()

python_folder = os.path.join(current_path, 'python')

if not os.path.exists(python_folder):
    os.mkdir(python_folder)

print("Folder created at:", python_folder)

main_file = os.path.join(python_folder, 'main.py')
mod_file = os.path.join(python_folder, 'my_mod.py')

open(main_file,'a')
open(mod_file,'a')


print("Main file path:", main_file)
print("Module file path:", mod_file)

#----------------------task 2 done ----------------
#--------------------------------------------------

'''
problem 03:
Import only the function say_welcome from the file my_mod.py 
into the main file main.py, and then call the function inside the main file.

'''
    

