# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def evenly_div_by(x,y):
    for i in range(1,y+1):
        if x % i != 0:
            break
    else:
        return True

i = 20
while evenly_div_by(i,20) != True:
    i += 20

print(i)
