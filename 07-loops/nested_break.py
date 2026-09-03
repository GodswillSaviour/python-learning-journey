# The outer loop generates values from 1 up to 3.
for outer in range(1, 4):

    # The inner loop generates values from 1 up to 3 for each outer value.
    for inner in range(1, 4):

        # Display the current values of both the outer and inner loops.
        print(outer, inner)

        # Check whether the inner loop has reached 2.
        if inner == 2:

            # Stop the inner loop when inner reaches 2.
            break