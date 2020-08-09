# Problem 11
# In the 20×20 grid below
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

import numpy

grid = open("problem10.txt").readlines() # Import grid

for i in range(20): # For every line (sublist) of the list
    grid[i] = grid[i].split(" ") # Separate it by spaces
    grid[i][19] = grid[i][19].replace("\n","")
    for j in range(20):
        grid[i][j] = int(grid[i][j])
    
def horizontal(x):
    
    horizontal_prods = [[0 for i in range(17)] for i in range(20)]
    
    for i in range(20):
        for j in range(17):
            horizontal_prods[i][j] = int(numpy.prod(x[i][j:j+4]))
            
    horizontal_max = []
    
    for i in range(20):
        horizontal_max.append(max(horizontal_prods[i]))
    
    highest_horizontal = [max(horizontal_max), 
                          horizontal_max.index(max(horizontal_max))]
    
    position = horizontal_prods[highest_horizontal[1]].index(highest_horizontal[0])
    
    return highest_horizontal, position

def vertical(x):
    transpose = numpy.array(x).T.tolist()
    return horizontal(transpose)

def diagonal(x):
    
    diagonal_prods = [[0 for i in range(17)] for i in range(17)]
    
    for i in range(16):
        for j in range(16):
            diagonal_elems = []
            for h in range(4):
                diagonal_elems.append(x[i+h][j+h])
            diagonal_prods[i][j] = int(numpy.prod(diagonal_elems))
    
    diagonal_max = []
    
    for i in range(16):
        diagonal_max.append(max(diagonal_prods[i]))
    
    highest_diagonal = [max(diagonal_max), 
                          diagonal_max.index(max(diagonal_max))]
    
    position = diagonal_prods[highest_diagonal[1]].index(highest_diagonal[0])
    
    return highest_diagonal, position
        
def diagonal_inverted(x):

    diagonal_prods = [[0 for i in range(17)] for i in range(17)]
    
    for i in range(17):
        for j in range(3,20):
            diagonal_elems = []
            for h in range(4):
                diagonal_elems.append(x[i+h][j-h])
            diagonal_prods[i][j-3] = int(numpy.prod(diagonal_elems))
    
    diagonal_max = []
    
    for i in range(16):
        diagonal_max.append(max(diagonal_prods[i]))
    
    highest_diagonal = [max(diagonal_max), 
                          diagonal_max.index(max(diagonal_max))]
    
    position = diagonal_prods[highest_diagonal[1]].index(highest_diagonal[0])
    
    return highest_diagonal, position    
    
    
h = list(horizontal(grid))
v = list(vertical(grid))
d = list(diagonal(grid))
i = list(diagonal_inverted(grid))

print("Largest horizontal product is " + str(h[0][0]) + " in row " + str(h[0][1]+1) + 
     " and in column " + str(h[1] + 1))
print("Largest vertical product is " + str(v[0][0]) + " in row " + str(v[1]+1) + 
     " and in column " + str(v[0][1] + 1))
print("Largest diagonal product is " + str(d[0][0]) + " in row " + str(d[0][1]+1) + 
     " and in column " + str(d[1] + 1))
print("Largest diagonal inverted product is " + str(i[0][0]) + " in row " + str(i[0][1]+1) + 
     " and in column " + str(i[1] + 4))

def largest_adjacent_prod(x):
    h = list(horizontal(x))
    v = list(vertical(x))
    d = list(diagonal(x))
    i = list(diagonal_inverted(x))
    products = [h[0][0], v[0][0], d[0][0], i[0][0]]
    largest = max(products)
    if largest == h[0][0]:
        print("Largest product is horizontal. It is " + str(h[0][0]) + " in row " + str(h[0][1]+1) + 
     " and in column " + str(h[1] + 1))
    elif largest == v[0][0]:
        print("Largest product is vertical. It is " + str(v[0][0]) + " in row " + str(v[1]+1) + 
     " and in column " + str(v[0][1] + 1))
    elif largest == d[0][0]:
        print("Largest product is diagonal. It is " + str(d[0][0]) + " in row " + str(d[0][1]+1) + 
     " and in column " + str(d[1] + 1))
    else:
        print("Largest product is diagonal inverted. It is " + str(i[0][0]) + " in row " + str(i[0][1]+1) + 
     " and in column " + str(i[1] + 4))

largest_adjacent_prod(grid)
