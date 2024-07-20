# Assigning a list of numbers
numbers = [1, 2, 3]

# Assigning a tuple containing a name, age, and profession
person = ("Jane", 25, "Python Dev")

# Assigning a string containing lowercase letters
letters = "abc"

# Assigning a dictionary with key-value pairs representing ordinal numbers
ordinals = {"one": "first", "two": "second", "three": "third"}

# Assigning a set containing even digits
even_digits = {2, 4, 6, 8}

# Assigning a list containing multiple variables as values
collections = [numbers, person, letters, ordinals, even_digits]

for collection in collections:
    for value in collection:
        print(value)