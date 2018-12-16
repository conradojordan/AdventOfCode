import time, re
from collections import defaultdict
startTime = time.time()

# Opens file and reads steps and its pre-requisites
file = open('input8example.txt')
nodesStr = file.read().strip().split()
file.close()
nodesData = []

for i in range(len(nodesStr)):
    nodesData.append(int(nodesStr[i]))

def parseNodes(node):
    if node[0] == 0:
        sumMeta = 0
        for i in range(2, 2+node[1]):
            sumMeta += node[i]
        return sumMeta
    else:
        sumMeta = 0
        for i in range(node[1]):
            sumInside = parseNodes(node[2:-node[1]])
            for j in range(len(node)-1, len(node)-1-node[1], -1):
                sumMeta += node[j]
        return sumMeta + sumInside

sumOfMetaData = parseNodes(nodesData)

## PART 1
print('\n-----Part 1-----')
print(nodesData)
print('len(nodesData) = ' + str(len(nodesData)))
print('Sum of all metadata = ' + str(sumOfMetaData))

print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')