# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
            break
    else:
        return True
    
numb = 2
prime = 1
position = 10002

while prime < position:
    if is_prime(numb) == True:
        prime += 1
    if prime < position:
        numb += 1
    
print(numb)
