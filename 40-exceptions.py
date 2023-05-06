'''
If we try to open a file that doens't exist, we got an error and the program crashs
To avoid that, we use try and except
'''

# 1st, the FileNotFoundError
file = open('wrong_file_name.txt', 'r')
print(file)
