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
'''
Problem 02:
Create a Function that name is get_people_scores
The function accepts a string parameter for the name and a variable number of keyword arguments that represent subjects
and their corresponding scores.
If no scores are provided, print "Hello [name] You Have No Scores To Show"
If scores are provided, print "Hello [name] Your Scores Are:" followed by each score in a new line
If the name parameter is an empty string, do not print the greeting message, just print the scores.
'''
def get_people_scores(name="", **scores):
    # Remove extra spaces from name
    name = name.strip()
    
    # Print scores only if name is empty
    if not name:
        if not scores:
            return  # No name and no scores, nothing to print
    else:
        # Print greeting with or without scores
        if not scores:
            print(f"Hello {name} You Have No Scores To Show")
            return
        print(f"Hello {name} Your Scores Are:")
    
    # Print scores if they exist
    for subject, score in scores.items():
        print(f"{subject} => {score}")

# Tests
get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Sandy")
get_people_scores("", Math=90, Science=80, Language=70)


# ----------------------task 2 done ----------------
#---------------------------------------------------------------
