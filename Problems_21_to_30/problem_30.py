# Problem 30

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_of_pow(number, power):
    str_num = str(number)
    total = 0
    for i in range(len(str_num)):
        total += pow(int(str_num[i]), power)
    if total == number:
        return True
    else:
        return False

total = 0
for i in range(2,1000000):
    if sum_of_pow(i, 5):
        total += i
print(total)
