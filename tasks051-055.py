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
# Problem 03:
# Create a dictionary named my_ranks that contains your ranks in the following subjects:
# Math: A
# Science: B
# Drawing: A
# Sports: C
# Calculate and print the total score based on the following rules:
# Rank A: 100 points
# Rank B: 80 points
# Rank C: 40 points

# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
# Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"



total_score = 0
for subject, rank in my_ranks.items():
    if rank == 'A':
        print(f"Your Rank in {subject} Is {rank}, And This Equal 100 Points.")
        total_score += 100
    elif rank == 'B':
        print(f"Your Rank in {subject} Is {rank}, And This Equal 80 Points.")
        total_score += 80
    elif rank == 'C':
        print(f"Your Rank in {subject} Is {rank}, And This Equal 40 Points.")
        total_score += 40
print(f"Total Score Is {total_score} Points.")

print("--------------------task 3 done -----------------------")
#---------------------------------------------------------------