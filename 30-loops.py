'''
Python has two primitive loop commands: for and while
'''

## for
# A 'for' loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the 'for' keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the 'for' loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

# Loopin through a string. Even strings are iterable objects, they contain a sequence of characters: 
print('\n')
for letter in "banana":
    print(letter)

# Break
# With the 'break' statement we can stop the loop before it has looped though all the items:
objects = ['keyboard', 'mouse', 'monitor', 'printer']
print('\n')
for obj in objects:
    print(obj)
    if obj == 'mouse':
        break


# Continue
# With the 'continue' statement we can stop the current iteration of the loop, and continue with the next:
objects = ['keyboard', 'mouse', 'monitor', 'printer']
print('\n')
for obj in objects:
    if obj == 'mouse':
      continue
    print(obj)


print('\n')
# Range
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6): # From 0 to 5
    print(x)

print('\n')
# with range fuction we can set start, end and increment values
for x in range(2, 30, 3):  # From 2 to 29, incrementing 3
  print(x)

print('\n')
# Nested Loops. Loop inside loop
# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)






## while
# With the while loop we can execute a set of statment as long as a condition is true.
print('\n')
i = 1
while i < 6:
    print(i)
    i += 1



## Break 
# With the 'break' statement we can stop the loop even if the while conditions is true:
print('\n')
a = 1
while a < 6:
    print(a)
    if a == 3:
        break
    a += 1
  
  


## Continue
# With the 'continue' statement we can stop the current iterarion, and continue with the next:
print('\n')
b = 0
while b < 6:
    b += 1
    if b == 3:
        continue
    print(b)                # Note that number 3 is missing in the result


## Else
# With the else statement we can run a block of code once when the condition no longer is true:
print('\n')

number = 1
while number < 6:
  print(number)  
  number += 1
  
  
else:
  print("The number is no longer less than 6")





print('\n')
#source: https://www.w3schools.com/python