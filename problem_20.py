# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

factorial_100 = 1
for i in range(1, 101):
    factorial_100 *= i
a = str(factorial_100) 
def split(x):
    return [int(i) for i in x]
print(sum(split(a)))
