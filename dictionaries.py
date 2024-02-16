import random

# Define an empty dictionary
var = {}

# Print the type of the variable var
print(type(var))

# Define a dictionary with key-value pairs
var2 = {"juice": "cranberry", "fruit": "mango", "movie": "The Lion King"}

# Print the dictionary var2
print(var2)

# Print the value associated with the key "fruit"
print(var2["fruit"])

# Add a new key-value pair to the dictionary var2
var2["drank"] = "Petron"

# Print the modified dictionary var2
print(var2)

# Update the value associated with the key "juice"
var2["juice"] = "apple"

# Print the modified dictionary var2
print(var2)

# Delete the key-value pair with the key "drank" from the dictionary var2
del var2["drank"]

# Print the modified dictionary var2
print(var2)

# Print the available methods for the dictionary var2
print(dir(var2))

# Print the keys of the dictionary var2 as a list
print(list(var2.keys()))

# Print the values of the dictionary var2 as a list
print(list(var2.values()))

# Print the key-value pairs of the dictionary var2 as a list of tuples
print(list(var2.items()))

# Print each key-value pair of the dictionary var2
for k, v in var2.items():
    print(k, v)
    
# Generate a dictionary with keys formatted as "key_i" and values as lists of 4 random integers between 0 and 10
dict_of_lists = {"key_{}".format(i): [random.randint(0, 10) for j in range(4)] for i in range(3)}  # complex code # dictionary comprehension

# Print the dictionary of lists
print(dict_of_lists)

# Print each key-value pair of the dictionary dict_of_lists and the elements of each list
for key, value in dict_of_lists.items():
    print(key, value)
    for i in value:
        print(i)
