import random



r1 = random.random()    # Give us a random number from 0 to 1
print(r1, '\n')

r2 = random.choice([1,2,3,4,5])     # Give us a random number from a list
print(r2, '\n')


r3 = random.randint(1, 5000)     # Give us a random number in a range
print(r3, '\n')



# Pick 10 random mumbers in a range
for r in range(10):                         
    number = random.randint(1, 1000)
    print(number)

print('\n')
# Pick every other year from 2005 until now - 2023
for i in range(2005, 2023, 2):           # range syntax: start, stop, step
    print(i)  