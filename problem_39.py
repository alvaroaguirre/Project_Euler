# Problem 39

# p is the perimeter of a right angle triangle, integer length sides {a,b,c}
# There are exactly three solutions for p = 120
# For which value of p <= 1000 is the number of solutions maximised?

from math import sqrt

def solutions(perimeter):
	solutions = 0
	for a in range(1, perimeter):
		for b in range(1,a):
			c = sqrt(a**2 + b**2)
			if a + b + c == perimeter:
				solutions += 1
	return solutions

max_sol = 0
for j in range(1, 1001):
	if solutions(j) > max_sol:
		max_sol = solutions(j)
		max_p = j

print(max_p)