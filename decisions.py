import random

# Generate a random number between 0 and 10
number = random.randint(0, 10)

# Threshold value for comparison
thresh = 7

# Decision-making process:

# Check if the generated number is greater than the threshold
if number > thresh:
    print("big number")
# If the number is less than the threshold
elif number < thresh:
    print("small number")
# If the number is equal to the threshold
else: # alternatively, could be elif number == thresh:
    print("number is thresh")

# Best practice: Use consistent indentation and comment style

# Additional decision-making:

# Check if the number is less than 3
if number < 3:
    print("really small number")

# Print the generated number
print(number)
