import random

number = random.randint(0, 10)

counter = 0

while number != 7:
    if counter >= 13:
        break
    
    number = random.randint(0, 10)
    counter = counter + 1 # counter += 1
    
print(counter, number)

for i in range(5):
    print(i ** 2)
    
letters = ["a", "b", "c", "d", "e"]

for letter in letters:
    print(letter.upper())