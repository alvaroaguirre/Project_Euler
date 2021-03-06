# Problem 29

# How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

def power(base, exponent):
    powers = []
    for a in range(2, base+1):
        for b in range(2, exponent+1):
            powers.append(pow(a,b))
    powers = set(powers)
    return len(powers)

print(power(100, 100))
