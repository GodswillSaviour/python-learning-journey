# Store the student's score and the maximum possible score.
score = 75
total = 100

# Calculate the student's percentage using arithmetic operators.
percentage = score / total * 100

# Compare the percentage with 50 to determine whether the student passed.
compare = percentage >= 50

# Display the student's score, percentage, and pass status.
print("Score:", score)
print("Percentage:", percentage)
print("Passed:", compare)

# Use the 'and' logical operator to check whether the score is within the valid range.
print("Valid score:", score >= 0 and score <= 100)