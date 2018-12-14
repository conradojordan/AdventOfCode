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

for line in lines:
    match = stepsRegex.search(line)
    stepsReq[match.group(2)].add(match.group(1))
    allSteps.add(match.group(1))
    allSteps.add(match.group(2))

## PART 2
print('-----Part 2-----')

currentSecond = 0
numWorkers = 5
stepDurationOffset = 60
currentSteps = set()
done = set()
workers = []
noReqs = []
stepsToRemove = []

for step in allSteps:
    if step not in stepsReq and step not in currentSteps:
        noReqs.append(step)
noReqs = sorted(noReqs)

# Initializing workers: [workingStep, timeLeft, isFree?]
for i in range(numWorkers):
    workers.append(['', 0, True])

def tryAllocateStep(worker):
    if worker[2]:
        if len(noReqs) > 0:
            step = noReqs[0]
            worker[0] = step
            worker[1] = ord(step.lower())-96+stepDurationOffset
            worker[2] = False
            currentSteps.add(step)
            del noReqs[0]

def tryDecrementTime(worker):
    if not worker[2]:
        worker[1] -= 1
        global timePassed
        timePassed = True

        if worker[1] == 0:
            finished = worker[0]
            worker[0] = ''
            worker[2] = True
            currentSteps.discard(finished)
            done.add(finished)

            for step in stepsReq:
                if finished in stepsReq[step]:
                    stepsReq[step].discard(finished)
                    if len(stepsReq[step]) == 0:
                        stepsToRemove.append(step)
                        noReqs.append(step)


# Loops through workers alocating step or decrementing time
while len(done) < len(allSteps):
    timePassed = False
    stepsToRemove = []

    for i in range(numWorkers):
        tryDecrementTime(workers[i])
    for i in range(numWorkers):
        tryAllocateStep(workers[i])

    if len(stepsToRemove) > 0:
        for removed in stepsToRemove:
            if removed in stepsReq:
                del stepsReq[removed]

    if timePassed:
        currentSecond += 1

print('Total number of seconds = ' + str(currentSecond))
print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')
print()