'''
 List operations are the operations that can be performed on the data in the list data structure.

Here is 
 A few of the basic list operations used in Python programming are: 
    extend(), insert(), append(), remove(), pop(), 
    slice, reverse(), len(), min() & max(), concatenate(), 
    count(), multiply(), sort(), index(), clear(), etc
'''

## ADD
# To add a single element at the end of the list use .append 
numbers = [1, 2]
print(numbers)

numbers.append(3)
numbers.append(4)
print(numbers)

for x in range(5,7):
    numbers.append(x)
print(numbers)


# The exntend() is used to add more than one element at the end of the list
numbers.extend([8,9])
print(numbers)


# The insert() method can add an element at a give position in the list
# syntax: list.insert({position}{element})
numbers.insert(5, 5.5)
print(numbers)


## DEL
# The remove() method is used to remove an element from the list. In the case of multiple occurrences of the same element, only the first occurrence is removed.
words = ['anger', 'fear' , 'joy', 'love', 'sadness', 'anger', 'fear' , 'joy', 'love', 'sadness']
print(words)
words.remove('anger')
print(words)

# The pop() method can remove an element from any given position
words.pop(5)
print(words)

# The slice op does not edit the list. It is used to print a section of the list.
print(numbers[:])       # prints from beginning to end of list
print(numbers[::-1])    # prints the list in the reverse order without modifying it
print(numbers[:4])      # prints from beginning to end index
print(numbers[4:])      # prints from start index to end of list
print(numbers[3:6])     # prints from start index to end index


## Reversing
# The reverse() method will reverse the elements of the list modifying it
numbers.reverse()
print(numbers)


## Others

# The len() methos is used to count the number of items on the list. The lenght of it.
print(numbers)
print(len(numbers))


# The min() and the max() methods are used to find the minimum and the maximum value in the list.
print(min(numbers))
print(max(numbers))


# The funciont count() returns the number of occurrences of a given element in the list
print(words)
print(words.count('joy'))


NumberWords = numbers + words
print(NumberWords)


# Python also allows multiplying the list n times. The resultant list is the original list iterated n times.
print(NumberWords*3)


# The index() method returns the position of the first occurrence of the given element
print(words)
print(words.index('love'))

print(numbers)
print(numbers.index(8, 0, 4))



# The sort method sorts the list in ascending order. This operation can only be performed on homogeneous lists, i.e. lists having elements of similar type.
print(numbers)
numbers.sort()
print(numbers)


# The clear() erases all the element from the list
print("NumberWords had:", NumberWords)
NumberWords.clear()
print("Now it has:", NumberWords)







# Source: https://www.educba.com/list-operations-in-python/