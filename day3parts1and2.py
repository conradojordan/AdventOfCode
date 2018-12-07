import numpy as np

# Opens file and saves claims in a list
file = open('input.txt')
claimsList = file.read().strip().split('\n')
file.close()

# Creates matrix with zeros
fabric = np.zeros((1000,1000))
overlapped = 0

# Parses the claims into 5 lists (cid, xo, yo, dx and dy) for easier use
cid, xo, yo, dx, dy = [[], [], [], [], []]
for claim in claimsList:
    claimSplit = claim.split()
    
    cid.append(claimSplit[0])
    coords = claimSplit[2][:-1].split(',')
    xo.append(int(coords[0]))
    yo.append(int(coords[1]))
    deltas = claimSplit[3].split('x')
    dx.append(int(deltas[0]))
    dy.append(int(deltas[1]))
    
# Increments square inch of the matrix for each time it is used in a claim
# First time it increments an element that was already used (i.e. sq inch = 1), it also
# increments the number of overlapped square inches.
# Further overlaps of same square inches are not counter (i.e. sq inch = 2, 3, 4...)

for i in range(len(cid)):
    for x in range(xo[i], xo[i]+dx[i]):
        for y in range(yo[i], yo[i]+dy[i]):
            if (fabric[x,y] == 1):
                overlapped += 1
            fabric[x,y] += 1

print('Square inches overlapped = ' + str(overlapped))


## PART 2
# For each claim, checks if it is not overlapped by any other claim

for i in range(len(cid)):
    uniqueClaim = True
    for x in range(xo[i], xo[i]+dx[i]):
        for y in range(yo[i], yo[i]+dy[i]):
            if (fabric[x,y] > 1):
                uniqueClaim = False
                break
        if (not uniqueClaim):
            break
    if(uniqueClaim):
        uniqueId = cid[i]

print('Unique claim ID = ' + uniqueId)
