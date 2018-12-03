import numpy as np

# Opens file and saves claims in a list
file = open('input.txt')
claimsList = file.read().strip().split('\n')

# Creates matrix with zeros
fabric = np.zeros((1000,1000))
overlapped = 0

# Increments square inch of the matrix for each time it is used in a claim
# First time it increments an element that was already used (i.e. sq inch = 1), it also
# increments the number of overlapped square inches.
# Further overlaps of same square inches are not counter (i.e. sq inch = 2, 3, 4...)

for claim in claimsList:
    claimSplit = claim.split()
    xo, yo = claimSplit[2][:-1].split(',')
    dx, dy = claimSplit[3].split('x')
    xo, yo, dx, dy = [int(xo), int(yo), int(dx), int(dy)]
    for x in range(xo, xo+dx):
        for y in range(yo, yo+dy):
            if (fabric[x,y] == 1):
                overlapped += 1
            fabric[x,y] += 1
