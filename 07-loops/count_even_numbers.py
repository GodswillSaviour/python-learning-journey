# Store the numbers that will be checked.
numbers = [3, 8, 12, 5, 7, 10, 14, 9]

# Start the counter at 0 before checking any numbers.
count = 0

# Process each number in the list one at a time.
for number in numbers:

    # Check whether the current number is even.
    if number % 2 == 0:

        # Increase the counter by 1 when an even number is found.
        count += 1

# Display the total number of even numbers.
print(count)