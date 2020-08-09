# Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def power_sum(x):
    a = str(2**x)
    count = 0
    for i in range(len(a)):
        count += int(a[i])
    return count

print(power_sum(1000))
