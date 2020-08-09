# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
            break
    else:
        return True
    
def factor_prime(x):
    for i in range(2,x):
        if x%i == 0:
            candidate = x // i
            if is_prime(candidate):
                print(candidate)
                break
                
factor_prime(600851475143)
