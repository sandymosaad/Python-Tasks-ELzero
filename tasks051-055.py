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
# Problem 04:
# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
for student, subjects in students.items():
    print("------------------------------")
    print(f"-- Student Name: {student}")
    print("------------------------------")
    total_score = 0
    for subject, rank in subjects.items():
        if rank == 'A':
            print(f'{subject} => {rank} => 100 Points')
            total_score += 100
        elif rank == 'B':
            print(f'{subject} => {rank} => 80 Points')
            total_score += 80
        elif rank == 'C':
            print(f'{subject} => {rank} => 40 Points')
            total_score += 40
        elif rank == 'D':
            print(f'{subject} => {rank} => 20 Points')
            total_score += 20
    print(f"Total Score For {student} Is {total_score} Points.")

#another solution
for student in students:
    print("------------------------------")
    print(f"-- Student Name: {student}")
    print("------------------------------")
    total_score = 0
    for subject in students[student]:
        rank = students[student][subject]
        if rank == 'A':
            print(f'{subject} => {rank} => 100 Points')
            total_score += 100
        elif rank == 'B':
            print(f'{subject} => {rank} => 80 Points')
            total_score += 80
        elif rank == 'C':
            print(f'{subject} => {rank} => 40 Points')
            total_score += 40
        elif rank == 'D':
            print(f'{subject} => {rank} => 20 Points')
            total_score += 20
    print(f"Total Score For {student} Is {total_score} Points.")
print("--------------------task 4 done -----------------------")
#---------------------------------------------------------------
#eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsImlhdCI6MTc1NzUxNzY5NCwiZXhwIjoxNzU3NTIxMjk0LCJpc3MiOiJmaXJlYmFzZS1hZG1pbnNkay02cjM0eUB0YWJuaW5lLWF1dGgtMzQwMDE1LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwic3ViIjoiZmlyZWJhc2UtYWRtaW5zZGstNnIzNHlAdGFibmluZS1hdXRoLTM0MDAxNS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsInVpZCI6InltMkdxblQ1a0JSbTVFR2ZWa0NXOFF1MGFPQzMifQ.ZnDapXK5ygt_Eiwxi-PZwxxj70JTA90NeByLSMU_ne-5KZpCpUsIUdaIznu5Atdceylf85SrxxpXRBaI4lZDWmDwZtnGVUgQ9B5zbun3Deu-eC_zRCNd-S872ajQHvCSZC3xHvTMZhk8E1Vpy6JRI8rfPFshIYV68gvVuHUsFEyUDCGgP2EM2nOzac8qfrp_wSS1h1Du6nAbFcb21-nFPHxi0rq6MOY_x0HbZSAm3K_E_R2DgiJCwPZ5FBQ477ssycr9B1Si4tb9Bax2ifAxA8QbRXQz9vMzV8SlNCk6fC9B47MmlSL_W8EWvPuZdUTYhtYuHLw6L0qUhK6gaG7g