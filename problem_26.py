# Problem 26

# A unit fraction contains 1 in the numerator
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import time

start = time.time()
from decimal import *
getcontext().prec = 1000

def get_decimal(x):
    '''Get the decimal part of 1/x as a string'''
    one_over = Decimal(1)/Decimal(x)
    return str(one_over)[2:-1]


def cycle_len(a, length):
    '''Check if string a has cycle of length'''
    substring = a[:length]
    b = set([a[j:j+length] for j in range(0, len(a), length)])
    tot = 0
    if len(b) <= 2:
        for ele in b:
            if len(ele) == len(substring):
                if ele == substring:
                    tot += 1
            else:
                if substring[:len(ele)] == ele:
                    tot += 1
        if tot == 2:
            return 1
        else:
            return 0
    else:
        return 0
    
def cycle(x):
    '''Return the length of cycle'''
    verify = [0 for i in range(1, len(x))]
    for i in range(1, len(x)):
        verify[i-1] = cycle_len(x, i)
    if sum(verify) >= 1:
        return verify.index(1)+1
    else:
        return 0

def primes(x): # Longest cycle will be in a prime number

    prime = [True for i in range(x+1)]
    p = 2
    prime[0] = False
    prime[1] = False
    while p <= x:
        if prime[p] == True:
            for i in range(p*2,x+1,p):
                prime[i] = False
        p += 1
    primes = []
    for i in range(x):
        if prime[i] == True:
            primes.append(i)
    return primes    

p = primes(1000)

longest_cycle = 0
value_of_d = 0
for d in range(len(p)):
    a = cycle(get_decimal(p[d]))
    if a > longest_cycle:
        longest_cycle = a
        value = p[d]
    
print('Number ' + str(value) + ' has a cycle of length ' + str(longest_cycle))
print(time.time() - start)
