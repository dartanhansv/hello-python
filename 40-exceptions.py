'''
If we try to open a file that doens't exist, we got an error and the program crashs
To avoid that, we use try and except
'''

'''
# 1st, the FileNotFoundError
file = open('wrong_file_name.txt', 'r')
print(file)


# 2nd, using try/except to prevent the program from failing
try:
    file = open('wrong_file_name.txt', 'r')
    print(file)
except:
    print("File doesn't exist")

'''

# The ValueError
price = input("Enter the price: ")      # an error would occur if the user typed a string for example
try:
    prince = float(price)
    print('Price = ', price)
except ValueError:                      # Looking for an specific error
    print('Not a number')
