# Problem 36

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def binary(x):
    return int(bin(x)[2:])

def palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
    
total = 0
for i in range(1000001):
    if palindrome(i) and palindrome(binary(i)):
        total += i

print(total)
