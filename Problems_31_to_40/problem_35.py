# Problem 35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

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

# Get list of primes below 2M
primes = sieve(1000000)

def rotation(x):
    '''Rotation function takes an integer and returns a list with all digit rotations (includes self)'''
    rotations = []
    initial = str(x)
    if len(initial) == 1:
        rotations.append(x)
        return rotations
    rotations.append(initial)
    for i in range(1,len(initial)):
        rotations.append(initial[1:len(initial)] + initial[0])
        initial = initial[1:len(initial)] + initial[0]
        if len(rotations) == len(initial):
            for i in range(len(rotations)):
                rotations[i] = int(rotations[i])
            return rotations
        
def circular_prime(x):
    '''Checks if a given number is a circular prime'''
    rotations = rotation(x)
    if all(rotations[i] in primes for i in range(len(rotations))):
        return True
    else:
        return False
    

count = 0

for i in range(len(primes)):
    if circular_prime(primes[i]):
        count += 1


print(count)
