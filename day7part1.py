import time, re
from collections import defaultdict
startTime = time.time()

# Opens file and reads steps and its pre-requisites
file = open('input.txt')
lines = file.read().strip().split('\n')
file.close()

stepsRegex = re.compile(r'Step (.) must be finished before step (.) can begin.')
stepsReq = defaultdict(set)
allSteps = set()
stepsInOrder = []

for line in lines:
    match = stepsRegex.search(line)
    stepsReq[match.group(2)].add(match.group(1))
    allSteps.add(match.group(1))
    allSteps.add(match.group(2))


while len(allSteps) > 0:
    noReqs = []
    stepsToRemove = []
    for step in allSteps:
        if step not in stepsReq:
            noReqs.append(step)
    nextStep = sorted(noReqs)[0]
    stepsInOrder.append(nextStep)
    for step in stepsReq:
        if nextStep in stepsReq[step]:
            stepsReq[step].discard(nextStep)
            if len(stepsReq[step]) == 0:
                stepsToRemove.append(step)
    for removed in stepsToRemove:
        if removed in stepsReq:
            del stepsReq[removed]
    allSteps.discard(nextStep)

finalSequence = ''
for s in stepsInOrder:
    finalSequence += s
    
## PART 1
print('\n-----Part 1-----')
print(finalSequence)

print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')