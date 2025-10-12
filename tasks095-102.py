'''
problem 01:
You have the following string:

text = "eeeeE llllll lllzzZzzzz eroe operationr pollo"


You need to find all the last letters from each group of letters before a space — plus the last letter of the entire text (as shown in the example image).

In other words, you want to extract every letter that comes right before a space or the end of the string.

'''
import re

text = "eeeeE llllll lllzzZzzzz eroe operationr pollo"

pattern = r"([A-Za-z])(?=\s|$)"
matches = re.findall(pattern, text)

print(matches)

#------------------Task 01 Done --------------
#---------------------------------------------
'''
problem 02:
You have the following string:

text = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"


Write a regular expression to match only the word "Elzero" that comes after the letter "L",
but without including the letter "L" in the result.
'''

text = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"

pattern = r"(?<=\bL)Elzero"
match = re.findall(pattern, text)

print(match)

#------------------Task 02 Done --------------
#--------------------------------------------

