import random

# Generate a random number between 0 and 10
number = random.randint(0, 10)

# Initialize counter
counter = 0

# Execute loop until number equals 7 or counter reaches 13
while number != 7:
    # Break the loop if counter exceeds 13
    if counter >= 13:
        break
    
    # Generate a new random number
    number = random.randint(0, 10)
    
    # Increment counter
    counter += 1  # shorthand for counter = counter + 1
    
# Print the number of iterations (counter) and the final number
print(counter, number)

# Iterate through the range of numbers from 0 to 4
for i in range(5):
    # Print the square of each number
    print(i ** 2)
    
# Define a list of letters
letters = ["a", "b", "c", "d", "e"]

# Iterate through each letter in the list
for letter in letters:
    # Print the uppercase version of each letter
    print(letter.upper())
