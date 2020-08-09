# Problem 27

# n^2 + an + b
# Primes for n from 0 to value d
# Find a*b s.th the largest sequence of primes is generated for abs(a), abs(b) < 1000 

def primes(x): # Creates sequence of primes up to number x
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

p = primes(10000)

def quadratic(n,a,b):
    return (n**2 + a*n + b)

def sequence(a,b):
    n = 0
    while quadratic(n,a,b) in p:
        n += 1
    return n

range_b = primes(1000)
for i in range(len(range_b)):
    negative = range_b[i] - 2*range_b[i]
    range_b.append(negative)


highest = 0
value_a = 0
value_b = 0

for a in range(-1000, 1000):
    for i in range(len(range_b)):
        if sequence(a,range_b[i]) > highest:
            highest = sequence(a,range_b[i])
            value_a = a
            value_b = range_b[i]
            
print(value_a, value_b, value_a*value_b)
