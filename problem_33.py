# Problem 33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
# it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import numpy as np

def naive_fraction(numerator, denominator):
    '''Returns True if the fraction can be naively simplified'''
    # If any is a multiple of 10 return False (trivial), or if they are the same
    if numerator % 10 == 0 or denominator % 10 == 0:
        return False
    # Get the true value of the division
    true_value = numerator/denominator 
    # Transform both into strings to manipulate
    num_str = str(numerator)
    denom_str = str(denominator)
    if len(set(num_str).intersection(set(denom_str))) == 0:
        return False
    # Get common digits, for this exercise only one possible common digit
    common_digits = list(set(num_str).intersection(set(denom_str)))[0]
    # Return false if no common factors or lenght of any is zero
    # New numerator and denominator
    if num_str.replace(common_digits,'') == '' or denom_str.replace(common_digits,'') == '':
        return False
    new_num = int(num_str.replace(common_digits,''))
    new_denom = int(denom_str.replace(common_digits,''))
    if new_denom == 0:
        return False
    new_value = new_num/new_denom
    if new_value == true_value:
        return True
    else:
        return False


# Find all fractions with value less than one and two digits in numerator/denominator that are naive
numerators = []
denominators = []

for i in range(10,100):
    for j in range(10,i):
        if naive_fraction(j,i):
            numerators.append(j)
            denominators.append(i)

def divisors(x):
    '''Find all divisors of x'''
    divisors = []
    for i in range(2,x+1):
        if x % i == 0:
            divisors.append(i)
    return divisors

def irreducible_fraction(numerator, denominator):
    '''Get the irreducible form of a fraction'''
    num_div = divisors(numerator)
    den_div = divisors(denominator)
    largest_common = list(set(num_div).intersection(set(den_div)))
    if len(largest_common) == 0:
        return numerator, denominator
    else:
        largest_common.sort()
        numerator = int(numerator/largest_common[-1])
        denominator = int(denominator/largest_common[-1])
        return irreducible_fraction(numerator, denominator)

numerator_product = np.prod(numerators)
denominator_product = np.prod(denominators)

num, denom = irreducible_fraction(numerator_product, denominator_product)
denom
