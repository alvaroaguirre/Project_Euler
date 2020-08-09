# Problem 4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
    
a = [i for i in range(999,900,-1)]
palin = []
for i in a:
    for j in a:
        if is_palindrome(str(i*j)):
            palin.append(i*j)
print(max(palin))
