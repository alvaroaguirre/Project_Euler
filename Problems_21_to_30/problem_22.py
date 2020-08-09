# Problem 22

# A text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

names = open("problem22.txt").readlines()
names = names[0].split(",")
for i in range(len(names)):
    names[i] = names[i][1:-1]
names.sort()

alphabet = ['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alph_value(y):
    x = y.lower()
    count = 0
    for i in x:
        count += alphabet.index(i)
    return count

total = 0
for i in range(len(names)):
    total += alph_value(names[i])*(i+1)
print(total)
