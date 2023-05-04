'''
What do *args and **kwargs stand for?

IE:
def myFunction(*args, *kwargs)
    # fuction 

"arg" and "kwargs" are common Python code terms, though they can be replaced with any other word precided by the asterisk/star (*).
The (*) takes a variable number of arguments
'''


def function_A(*args):
    print(args)

function_A('A','B','C')
print('\n')

function_A('A','B','C', 'D', 'E','F')
print('\n')