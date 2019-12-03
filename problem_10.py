# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
start = time.time()

def sieve(x):

    prime = [True for i in range(x+1)]
    p = 2
    prime[0] = False
    prime[1] = False
    while p <= x:
        if prime[p] == True:
            for i in range(p*2,x+1,p):
                prime[i] = False
        p += 1
    sum = 0
    for i in range(x+1):
        if prime[i]:
            sum += i
    return sum

print(sieve(2000000))
print(time.time() - start)
