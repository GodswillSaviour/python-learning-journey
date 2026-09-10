# Store the number whose multiplication table we want to create.
number = 5

# Repeat the loop for multipliers from 1 up to 10.
for multiplier in range(1, 11):

    # Calculate the result of multiplying number by the current multiplier.
    result = number * multiplier

    # Display the multiplication calculation and its result.
    print(number, "x", multiplier, "=", result)