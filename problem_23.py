# Problem 23

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28
# which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n 
# and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24
# By mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that 
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time
start = time.time()

def d(n):
    proper_div = 0
    for i in range(1,n):
        if n % i == 0:
            proper_div += i
    return proper_div

def abundant(n):
    if d(n) > n:
        return True
    else:
        return False

ab_numbs = [False for i in range(1,28124)]

for i in range(len(ab_numbs)):
    if abundant(i):
        ab_numbs[i] = True
        
a = [i for i, x in enumerate(ab_numbs) if x]

b = []

for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] + a[j] < 28124:
            b.append(a[i] + a[j])

b = set(b)

sum_28123 = 28123*28124/2
print(sum_28123 - sum(b))

print(time.time() - start)
