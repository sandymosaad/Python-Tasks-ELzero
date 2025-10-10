
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

'''
problem 03:
You have an image of size 1200x800.
Each letter is inside a 400x400 box.
- Crop the letter "L"
- Convert it to grayscale
- Save it beside the original image
- Then crop the second row of letters
- Rotate it 180 degrees, convert to grayscale
- Save the result beside the original image
'''

from PIL import Image
import os

# Define paths
base_path = r"E:\ITI\Pytho-Tasks-ElZero"
img_path = os.path.join(base_path, "elzero-pillow.png")

# Open and show the image
my_img = Image.open(img_path)
#my_img.show()

# === 1️⃣ Crop letter L (top-right 400x400 box) ===
L_box = (400, 0, 800, 400)
cropped_L = my_img.crop(L_box)

# Convert to grayscale and save
gray_L = cropped_L.convert("L")
gray_L_path = os.path.join(base_path, "Letter_L_grayscale.png")
gray_L.save(gray_L_path)
#gray_L.show()

# === 2️⃣ Crop second row (bottom 400px) ===
row_box = (0, 400, 1200, 800)
cropped_row = my_img.crop(row_box)

# Convert to grayscale and rotate 180 degrees
gray_rotated_row = cropped_row.convert("L").rotate(180)

# Save and show
gray_rotated_row_path = os.path.join(base_path, "grayscale_cropped_row_image_rotated.png")
gray_rotated_row.save(gray_rotated_row_path)
#gray_rotated_row.show()

print(" Letter L and second row processed successfully!")
#-----------------task 03 done -------------
#------------------------------------------

'''
problem 04:
create a function that accepts a name as a parameter and returns the string "Hello {name}"
Also, add a docstring to the function to explain its purpose.
'''


def say_hello_to(name):
    """
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    """
    return f"Hello {name}"

print(say_hello_to("Osama"))  # "Hello Osama"

# Function Doc String Output
print(say_hello_to.__doc__)
