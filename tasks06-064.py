'''
Problem 01:
# Create a Function that name is get_score
# The function accepts a variable number of keyword arguments that represent subjects and their corresponding scores.
# The function should print each subject and its corresponding score in a new line.
'''
def get_score(**scores):
    for subject, score in scores.items():
        print(f"{subject} => {score}")
# Tests
get_score(Math=90, Science=80, Language=70)

# Output
"Math => 90"
"Science => 80"
"Language => 70"

print("--------------------task 1 done -----------------------")
#---------------------------------------------------------------

