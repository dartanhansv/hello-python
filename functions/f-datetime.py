from datetime import date


'''
Ask the user for input
Store user input in a variable
'''
print('\n')
born = input('What year were you born in? ')
today = date.today()

print('\n', "Therefore you are ", today.year - int(born), " year old. Still young, but for how many moons?", '\n')