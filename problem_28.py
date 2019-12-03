# Problem 28

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Note that a 5x5 spiral diagonal sum is composed by (2 + 4)*4
# Since it grows as a square it will always be multiplied by 4

def diagonal_sum(x):
    """x is the size of the spiral. Has to be an odd number."""
    terms = x//2
    total = 1
    count = 1
    final = 1
    while count <= terms:
        for i in range(4):
            total += count*2
            final += total
        count += 1
    return final

print(diagonal_sum(1001))
