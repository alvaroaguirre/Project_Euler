# Problem 37

# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously remove digits from left to right, 
# and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
        
def sieve(x):
    '''Sieve of Eratosthenes to get primes below x'''
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
    for i in range(x+1):
        if prime[i]:
            primes.append(i)
    return primes

primes = sieve(799999)

subset_primes = []

for i in range(len(primes)):
    temp = str(primes[i])
    if '4' not in temp and '6' not in temp:
        subset_primes.append(primes[i])
        
def truncate_right(x):
    number = str(x)
    truncates = []
    for i in range(1,len(number)):
        truncates.append(int(number[:len(number)-i]))
    return truncates

def truncate_left(x):
    number = str(x)
    truncates = []
    for i in range(len(number)):
        truncates.append(int(number[i:]))
    return truncates

def truncate(x):
    left = truncate_left(x)
    right = truncate_right(x)
    return left + right

def truncatable(x):
    '''Checks if a given number is a truncatable prime'''
    if x < 10:
        return False
    truncations = truncate(x)
    if all(truncations[i] in primes for i in range(len(truncations))):
        return True
    else:
        return False

    
total = []
for i in range(len(subset_primes)):
    if truncatable(subset_primes[i]):
        total.append(subset_primes[i])
        
sum(total)
