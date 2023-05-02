

def average(numbers):
    avg = sum(numbers)/len(numbers)
    return avg

'''
def average(numbers):
    total = 0

    for num in numbers:
        total = total + num

        avg = total/len(numbers)
        return avg
'''

prices = [1,2,3,4,5]

print(average(prices))