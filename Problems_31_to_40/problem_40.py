# Problem 40

# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

a = [str(i) for i in range(1,2000000)]
decim_frac = "".join(a)
print(len(decim_frac))

index = [10**j for j in range(7)]

total = 1
for i in range(len(index)):
	total *= int(decim_frac[index[i]-1])

print(total)