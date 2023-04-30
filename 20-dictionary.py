'''
A Dictionary maps keys to values
syntax: myDict = {key:value}
'''


# Create an empty dict
musketeers = {}

# Addind dictionary items
musketeers['Athos'] = 'The Leader and best swordsman'
musketeers['Porthos'] = 'The extrovert'
musketeers['Aramis'] = 'The Priest'
musketeers["D'Artagnan"] = 'The Brave hothead'
print(musketeers)

# To look up a value in a dict, we send in a key
print(musketeers['Porthos'])

# To update the key value, just add the new value
musketeers['Porthos'] = 'The Outgoing '
print(musketeers['Porthos'])


# Removing Dict items
musketeers['Tréville'] = "The Boss"
print(musketeers)

del musketeers['Tréville']
print(musketeers)

# Get an item that might not be there
# If you try to access a key in dict that's not there, you'll get a key error, and your program will quit.
# uncomment next line to check it
# musketeers['Tréville']

# To avoid that, use the get() method:
tryKey = musketeers.get('Tréville') # it will return "None", meaning the absence of a value.
print(tryKey)

# None evaluates to false in a conditional
if tryKey :
    print(tryKey)
else:
    print("Key doesn't exit")








'''
 Source: Python: Using Lists, Dictionaries, Loops, Files, and Modules (Interactive) by Sarah Holderness
https://www.pluralsight.com/interactive-courses/python-list-loop-function-data-module
'''