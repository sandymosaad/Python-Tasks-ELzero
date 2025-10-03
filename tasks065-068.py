'''
Problem 1:
- Create Python folder on desktop
- Create assign.py inside Python folder
- Create 50 text files (txt1 to txt50)
- Write "Elzero Web School => {number}" in each file
- Make file 25 empty and name it special-text
- Print current working directory, file path, filename, and total files count
'''

'''
import os
'''
import os

# Get desktop path and create Python folder
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
python_folder = os.path.join(desktop_path, "Python")
os.makedirs(python_folder, exist_ok=True)

def create_text_files():
    # Create assign.py first
    assign_path = os.path.join(python_folder, "assign.py")
    open(assign_path, 'w').close()

    """Create 50 text files with specified content"""
    # Create 50 text files
    for i in range(1, 51):
        if i == 25:
            # Create special empty file
            filename = "special-text.txt"
            open(os.path.join(python_folder, filename), 'w').close()
        else:
            # Create normal numbered files
            filename = f"txt{i}.txt"
            with open(os.path.join(python_folder, filename), 'w') as f:
                f.write(f"Elzero Web School => {i}\n")
                f.write(os.getcwd() + "\n")  # Current working directory
                f.write(os.path.dirname(f.name) + "\n")  # File path
                f.write(os.path.basename(f.name) + "\n")  # File name
    
    # Print total files count
    files_count = len([f for f in os.listdir(python_folder) if os.path.isfile(os.path.join(python_folder, f))])
    print(f"Total Files Count: {files_count}")

# Execute the function
create_text_files()
print(f"Files created in: {python_folder}")

#--------------------------problem 1 done -----------------------
#---------------------------------------------------------------
"""
Problem 2:
- Open txt1.txt file
- Keep first line (Elzero Web School => 1)
- Append 'Appended => Elzero Web School' 50 times
- Each append on a new line
"""

def append_to_file():
    with open(os.path.join(python_folder, 'txt1.txt'), 'a') as file:
        for _ in range(50):
            file.write('Appended => Elzero Web School\n')

append_to_file()
print("--------------------problem 2 done -----------------------")
#--------------------------------------------------------------

"""
Problem 3:
- Open txt1.txt and analyze its content
- Print number of lines
- Print number of words
- Print number of characters
- Print number of 'l' characters (case insensitive)
"""

def read_info_file():
    with open(os.path.join(python_folder, 'txt1.txt'), 'r') as file:
        # Read content once
        content = file.read()
        # Reset file pointer to start
        file.seek(0)
        # Get lines
        lines = file.readlines()
        
        # Calculate all required information
        print(f"Number Of Lines Is => {len(lines)}")
        print(f"Number Of Words Is => {len(content.split())}")
        print(f"Number Of Characters Is => {len(content)}")
        print(f"Number Of 'l' Char Is => {content.lower().count('l')}")

read_info_file()
print("--------------------problem 3 done -----------------------")
#-------------------------------------------------------------------

'''
problem 4:
delete last 10 files 

'''

import re
txt_files = [f for f in os.listdir(python_folder) if f.endswith(".txt")]


txt_files = [f for f in os.listdir(python_folder) if re.match(r"^txt\d+\.txt$", f)]

# ترتيب حسب الرقم
txt_files.sort(key=lambda x: int(re.search(r"\d+", x).group()))
last_10_files = txt_files[-10:]

for file in last_10_files:
    os.remove(os.path.join(python_folder, file))
    print(f"Deleted: {file}")