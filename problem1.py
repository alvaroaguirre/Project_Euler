# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

multiples = []

def multiples_3_5(x):
    a = 0
    while a < x:
        if a % 3 == 0:
            multiples.append(a)
        elif a % 5 == 0:
            multiples.append(a)
        a += 1
    return sum(multiples)

print(multiples_3_5(1000))
