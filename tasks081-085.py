'''
problem 01:
Use the yield keyword with what you’ve learned to reverse a string.
After that, make sure the loop works successfully and outputs the required result.

'''
def reverse_string(my_string):
    for char in my_string[::-1]:
        yield char
# Reverse The String
for c in reverse_string("Elzero"):
  print(c)

print('----------------------')
# another solution
def reverse_string(my_string):
    for char in reversed(my_string):
        yield char

for c in reverse_string("Elzero"):
  print(c)
#--------------------task 1 done ----------------
#-------------------------------------------------

