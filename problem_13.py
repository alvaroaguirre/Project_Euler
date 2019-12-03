# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

numbers = open("problem13.txt").readlines()

for i in range(100):
    numbers[i] = numbers[i].replace("\n","")
    numbers[i] = int(numbers[i])

print(str(sum(numbers))[:10])
