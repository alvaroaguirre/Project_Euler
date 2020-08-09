# Problem 25

# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

f_t0 = 1
f_t1 = 1

iteration = 2
while len(str(f_t1)) < 1000:
    hold = f_t1
    f_t1 += f_t0
    f_t0 = hold
    iteration += 1
    
print(iteration)
