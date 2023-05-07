
print('\n')
# Formatted Strings
nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'Programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + '[' + profissao + ']'
print(texto)

texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'
print(texto2)

print('\n')

# Metodos para strings
mensagem = "Eu adoro comida Caseira"

# Metodo "original"
print(mensagem)

# Metodo "tudo minusculo"
print(mensagem.lower())

# Metodo "tudo maiusculo"
print(mensagem.upper())

# Metodo "Inverter case"
print(mensagem.swapcase())


# Metodo "Substituir"
print(mensagem.replace('Caseira', 'mineira'))










print('\n')
###############################################################################################################################
# going further
# source:  https://towardsdatascience.com/5-advanced-string-methods-in-python-5b7f6ef382e1

'''
1. Variables in String 
Insert/replace a variable in place.
'''


name = "Alexander Hamilton"
print(f"Hello {name}")
# Hello Alexander Hamilton
print('\n')
'''
 2. Variable Formatting in String
 Format a variable such as an integer in place
'''

# 2.1 Print a large integer with commas:
x = 2*10**5
print(f"You have ${x:,} in your bank account")
# You have $200,000 in your bank account
# ** is Exponentiation;  2 ** 5 = 2*2*2*2*2
print('\n')

# 2.2 Print a float with a specified number of digits:
pi = 3.1415926535897932384 
print(f"The first 5 digits of pi are {pi:.5f}")
# The first 5 digits of pi are 3.14159
print('\n')

#3. In Place Boolean Logic:
'''
Perhaps you want to format a string based on several conditions. 
F-string notation allows for in place boolean arguments, just as you would expect from lambdas

'''
new_user = False
user_name = "Alexander Hamilton"
print(f"{'Congrats on making your account' if new_user else 'Welcome back'} {user_name}!")
# Welcome back Alexander Hamilton!
print('\n')
new_user = True
user_name = "Kimi Räikkönen"
print(f"{'Congrats on making your account' if new_user else 'Welcome back'} {user_name}!")
# Congrats on making your account Kimi Räikkönen!
print('\n')

# 4. Printing Variable Names & Values
# As of python 3.8, f-string notation allows printing of variable names with their values — an especially useful tool for debugging:
max_price = 20000
min_price = 4000
print(f"{max_price=:,}  |  {min_price=:,}")
# max_price=20,000  |  min_price=4,000
print('\n')
# 5. Formatting Variables in Pre-populated Strings (MailMerge)
'''
String formatting allows replacement of variables in pre-populated strings.
This is especially useful for allowing external users to format an email message which the program will fill in
'''

# 5.1 Str.Format Method (Preferred)
my_message = "Welcome to our platform {FNAME}! Your favorite ice cream flavor is {FLAVOR}."
FNAME = "Alexander"
FLAVOR = "Mint Chocolate Chip"
my_message_formatted = my_message.format(**{"FNAME":FNAME, "FLAVOR":FLAVOR})
print(my_message_formatted)
# Welcome to our platform Alexander! Your favorite ice cream flavor is Mint Chocolate Chip.
print('\n')

########################################################################################################################################


