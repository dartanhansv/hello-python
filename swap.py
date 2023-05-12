## How to swap two variables?


# Ask the user for the value of the variables
A = int(input("Please, enter the value of A: "))
B = int(input("Please, enter the value of B: "))

# Print the original values
print("\n Before swap \n a = %d \n b = %d" %(A, B))

# swap the values
A, B = B, A

# Print the values after swapping them 
print("\n After swapping \n a =", A, "\n b =", B, '\n')