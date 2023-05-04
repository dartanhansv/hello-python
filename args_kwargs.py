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


'''
kwargs stands for keyword arguments
The only difference from args is that it uses keywords and returns the values in the form of a Dictionary
'''



def function_B(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs)

function_B(First='Dartanhan', Middle='S.', Last='Venturini')


print('\n')
def function_C(**kwargs):
    for key, value in kwargs.items():
        #print(key)
        #print(value)
        print("The value of {} is {}" .format(key, value))

function_C(First_name='Dartanhan', Middle_name='S.', Last_name='Venturini')





# Bear in mind: *args creates tuple wheareas **kwargs creates dictionary