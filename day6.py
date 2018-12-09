import time
from collections import defaultdict
startTime = time.time()

# Manhattan distance function
def manhattanDistance(pointA, pointB):
    return abs(pointA[0]-pointB[0]) + abs(pointA[1]-pointB[1])

# Sum of manhattan distances
def sumManhattan (point):
    sumM = 0
    for c in coord:
        sumM += manhattanDistance(point, c)
    return sumM

# Opens file and reads coordinates, saves in list called 'coord'
file = open('input.txt')
coord = file.read().strip().split('\n')
file.close()
for i in range(len(coord)):
    coord[i] = coord[i].split(',')
    coord[i][0], coord[i][1] = int(coord[i][0]), int(coord[i][1])

# Finds maximum and minimum values of x and y from the coordinates
xMin, xMax, yMin, yMax = coord[0][0], coord[0][0], coord[0][1], coord[0][1]
for c in coord:
    if (c[0] < xMin):
        xMin = c[0]
    elif (c[0] > xMax):
        xMax = c[0]
    if (c[1] < yMin):
        yMin = c[0]
    elif (c[1] > yMax):
        yMax = c[0]

# Delimits a square that contains all points. Calculates the area
# associated to the points inside the square.
# Checks all the areas that touch the border of the square, these areas will be infinite.
areas = defaultdict(int)
infiniteAreas = set()

for coordinateX in range(xMin, xMax+1):
    for coordinateY in range(yMin, yMax+1):
        currentPoint = [coordinateX, coordinateY]
        tied = 0
        minDist = manhattanDistance(currentPoint, coord[0])
        for i in range(len(coord)):
            currentDistance = manhattanDistance(currentPoint, coord[i])
            if (currentDistance < minDist):
                minDist = currentDistance
                minDistIndex = i
                tied = 0
            elif (currentDistance == minDist):
                tied = 1
        if (not tied):
            areas[minDistIndex] += 1
            if ((coordinateX == xMin) or (coordinateX == xMax) or (coordinateY == yMin) or (coordinateY == yMax)):
                infiniteAreas.add(minDistIndex)

# Remove points with infinite areas from the dictionary
for point in infiniteAreas:
    del areas[point]

# Finds maximum area and point associated
maximumArea = 0
for item in areas.items():
    if (item[1] > maximumArea):
        maximumArea = item[1]
        pointIndex = item[0]

pointMaxArea = coord[pointIndex]

## PART 1
print('-----Part 1-----')
print('Maximum area = ' + str(maximumArea))
print('Point associated with maximum area = ' + str(pointMaxArea))

## PART 2
region = 0
limit = 10000

# Calculate region inside square
for coordinateX in range(xMin, xMax+1):
    for coordinateY in range(yMin, yMax+1):
        currentPoint = [coordinateX, coordinateY]
        if (sumManhattan(currentPoint) <= limit):
            region += 1

# Keep calculating border of incremented squares until no more region is outside
hasRegion = True
sqInc = 1
while (hasRegion):
    hasRegion = False
    for x in range(xMin-sqInc,xMax+sqInc+1):
        if (sumManhattan([x, yMin-sqInc]) < limit):
            region += 1
            hasRegion = True
        if (sumManhattan([x, yMax+sqInc+1]) < limit):
            region += 1
            hasRegion = True
    for y in range(yMin-sqInc+1,yMax+sqInc):
        if (sumManhattan([xMin-sqInc,y]) < limit):
            region += 1
            hasRegion = True
        if (sumManhattan([xMax+sqInc,y]) < limit):
            region += 1
            hasRegion = True
    sqInc += 1

print('-----Part 2-----')
print('Region size with limit ' + str(limit) + ' = ' + str(region) + '\n')
print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')
