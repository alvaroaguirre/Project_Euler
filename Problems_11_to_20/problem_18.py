# Problem 18
# Find the maximum total from top to bottom of the triangle below. Only moving through adjacent points.


triangle = open("problem18.txt").readlines()

for i in range(len(triangle)):
    triangle[i] = triangle[i].replace('\n','').split()
    for j in range(len(triangle[i])):
        triangle[i][j] = int(triangle[i][j])

def recursive_triangle(y):
    x = y
    for i in range(len(x)-2,-1,-1):
        for j in range(len(x[i])):
            x[i][j] = max(x[i][j] + x[i+1][j], x[i][j] + x[i+1][j+1])
    return x[0][0]

recursive_triangle(triangle)
