## Compare

# Lists
# For two list to be equal, they have to have exactly the same items in exactly the same order. 
my_list = [1, 2, 3, 4]
your_list = [4, 3, 2, 1]
his_list = [1, 2, 3, 4]
print(my_list == your_list)         # Returns False
print(my_list == his_list)          # Returns True
print("\n")

# Dictionaries
# Order doesn't matter
my_dict = {1:1, 2:2, 3:3, 4:4}
your_dict = {1:1, 2:2, 3:3, 4:4}
print(my_dict == your_dict)          # Returns True
print("\n")


## Combine
# List of Lists
breakfast = ['Spam n Eggs', 'Spam n Jam', 'Spam n Ham']
lunch  = ['SLT (Spam-Lettuce-Tomato)', 'PB&S (PB&Spam)']
dinner = ['Spalad', 'Spamghetti', 'Spam noodle soup']

menus = [['Spam n Eggs', 'Spam n Jam', 'Spam n Ham'], ['SLT (Spam-Lettuce-Tomato)', 'PB&S (PB&Spam)'], ['Spalad', 'Spamghetti', 'Spam noodle soup']]

# Select a item(the whole list) from the list of lists
print('Breakfast Menu:\t', menus[0])
print('Lunch Menu:\t', menus[1])
print('Dinner Menu:\t', menus[2])
print("\n")

# Select a item from the inner list
print(menus[1][0])         
# Print the first item from the second list! It work, but we have to know that 'Lunch' is the second inner list
# With Dictionary we don't need to know where the items are
print("\n")


# Dict of Lists
dict_menu = {'Breakfast':['Spam n Eggs', 'Spam n Jam', 'Spam n Ham'], 'Lunch':['SLT (Spam-Lettuce-Tomato)', 'PB&S (PB&Spam)'], 'Dinner': ['Spalad', 'Spamghetti', 'Spam noodle soup']}

print('Breakfast Menu:\t', dict_menu['Breakfast'])
print('Lunch Menu:\t', dict_menu['Lunch'])
print('Dinner Menu:\t', dict_menu['Dinner'])
print("\n")







print("\n")
'''
 Source: Python: Using Lists, Dictionaries, Loops, Files, and Modules (Interactive) by Sarah Holderness
https://www.pluralsight.com/interactive-courses/python-list-loop-function-data-module
'''
