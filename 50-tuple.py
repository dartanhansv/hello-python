"""
Tuple
    Immutable sequences of arbitrary objects delimeted by parentheses
    Once created, the objects within them cannot be replaced or removed, and new elements cannot be added.
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


# Nested tuples
print('\n')
all = ((3, 15, 53, 55, 62, 74), ("Blue Valley", "Evergreen City", "Gotham City", "Smallville"), (3, "Gotham", 15, "Smmallville", 10.5))
print(all, '\n')
print(all[2][1], '\n')


# Tuple Unpacking - Extract value back into variables   - https://www.w3schools.com/python/python_tuples_unpack.asp
# Packing
fruits = ("apple", "banana", "cherry")
# unpacking
(green, yeloow, red) = fruits
print(green)
print(yeloow)
print(red)
print('\n')

# The number of variables must match the number of values in the tuple, if not, you most use an asterisk to collect the remaining values as a list
more_fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yeloow, *red) = more_fruits
print(green)
print(yeloow)
print(red)
print('\n')