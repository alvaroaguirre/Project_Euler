# Problem 32

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
def pandigital_9(x):
    nums = [i for i in range(1,10)]
    a = list(str(x))
    for i in range(len(a)):
        a[i] = int(a[i])
    a.sort()
    return a == nums

def pandigital_product(multiplicand, multiplier):
    product = multiplicand * multiplier
    a = str(multiplicand) + str(multiplier) + str(product)
    return pandigital_9(a)

pandigitals = []
for i in range(1,9999):
    limit = 9999//i
    for j in range(1,limit):
        if pandigital_product(i,j):
            pandigitals.append(i*j)
            
print(sum(list(set(pandigitals))))
