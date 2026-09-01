# Store the student's score.
score = 10

# Check if the score is 70 or higher.
if score >= 70:
    print("Excellent")

# If the first condition is false, check if the score is 50 or higher.
elif score >= 50:
    print("Pass")

# If all previous conditions are false, the score is below 50.
else:
    print("Fail")