# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(x):
    sum_sq = 0
    for i in range(1,x+1):
        sum_sq += i**2
    return sum_sq

def square_sum(x):
    return (sum(range(1,x+1))**2)

def sq_diff(x):
    return abs(sum_squares(x) - square_sum(x))

sq_diff(100)
