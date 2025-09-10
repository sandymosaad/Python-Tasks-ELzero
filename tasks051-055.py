# Problem 01:
# Create a list named my_nums that contains the following numbers:
# 15, 81, 5, 17, 20, 21, 13, 30, 65, 10, 7, 9.
# Sort the list in descending order.
# Use a for loop to print all the numbers that are multiples of 5.
# Finally, print a message that all numbers have been printed successfully. 
my_nums = [15, 81, 5, 17, 20, 21, 13, 30, 65, 10, 7, 9]
my_nums.sort(reverse=True)

count = 1
for num in my_nums:
    if num % 5 == 0:
        print(f"{count} => {num}")
        count += 1
print("All Numbers Printed Successfully.")
print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------
# Problem 02:
# Use a for loop to print all the numbers from 1 to 20.
# Skip the numbers 6, 8, and 12.
# Use the zfill() method to print the numbers with leading zeros.

for num in range(1, 21):
    if num == 6 or num == 8 or num == 12:
        continue
    #print(num, type(num))
    print(str(num).zfill(2))
print("--------------------task 2 done -----------------------")
#---------------------------------------------------------------