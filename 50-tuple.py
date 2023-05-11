"""
Tuple
    Immutable sequences of arbitrary objects
    Tuples are delimeted by parentheses
"""

## Tuple 

# An empty Tuple
fears = ()

# Tuple containing numbers
lottery = (3, 15, 53, 55, 62, 74)

# Tuple containing strings
cities = ("Blue Valley", "Evergreen City", "Gotham City", "Smallville")

# Tuple containing mixed items
both = (3, "Gotham", 15, "Smmallville", 10.5)


## Index 
# Same as lists - We can access the elements of a tuple by 0-based index using square brackets
print("The first element of the tuple 'cities' is:", cities[0])

# We can determine the number of elements in the tuple using len()
print('The tuple "Both" has', len(both), 'alements')

# Loop tuple
for item in cities:
    print(item)