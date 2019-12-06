# Problem 34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

def curious_number(x):
    '''Function that checks if an integer satisfies this curious property'''
    number = list(str(x))
    summation = 0
    for digit in number:
        summation += factorial(int(digit))
    if summation == x:
        return True
    else:
        return False
    
numbers = []
# Number can't be larger than 10e5
for i in range(3,100000):
    if curious_number(i):
        numbers.append(i)

print(sum(numbers))
