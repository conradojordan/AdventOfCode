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

## PART 2
print('\n\n-----Part 2-----')

stepsReq2 = defaultdict(set)
allSteps2 = set()
stepsInOrder = []

for line in lines:
    match = stepsRegex.search(line)
    stepsReq2[match.group(2)].add(match.group(1))
    allSteps2.add(match.group(1))
    allSteps2.add(match.group(2))

currentSecond = 0
currentSteps = set()
done = set()
workers = []
numWorkers = 5
noReqs = []

for step in allSteps2:
    if step not in stepsReq2 and step not in currentSteps:
        noReqs.append(step)
noReqs = sorted(noReqs)

# Initializing workers: [workingStep, timeLeft, isFree?]
for i in range(numWorkers):
    workers.append(['', 0, True])

for i in range(numWorkers):
    if workers[i][2]:
        if len(noReqs) > 0:
            nextStep = noReqs[0]
            workers[i][0] = nextStep
            workers[i][1] = ord(nextStep.lower())-36
            workers[i][2] = False
            currentSteps.add(nextStep)
            del noReqs[0]



#TODO: verificar essa variavel de critério de parada abaixo
while len(done) < len(allSteps2):

    stepsToRemove = []
    print('\n\ncurrentSecond = ' + str(currentSecond))
    print('allSteps = ' + str(allSteps2))
    print('stepsReq = ' + str(stepsReq2))
    print('noReqs = ' + str(noReqs))

#TODO: verificar a lógica: iniciar alocando todo mundo. passa - se tiver, subtrai, se não aloca E subtrai
    for i in range(numWorkers):
        if workers[i][2]:
            if len(noReqs) > 0:
                nextStep = noReqs[0]
                workers[i][0] = nextStep
                workers[i][1] = ord(nextStep.lower())-36
                workers[i][2] = False
                currentSteps.add(nextStep)
                del noReqs[0]
    for i in range(numWorkers):
        if not workers[i][2]:
            workers[i][1] -= 1
            if workers[i][1] == 0:
                finished = workers[i][0]
                workers[i][0] = ''
                workers[i][2] = True
                currentSteps.discard(finished)
                done.add(finished)
                for step in stepsReq2:
                    if finished in stepsReq2[step]:
                        stepsReq2[step].discard(finished)
                        if len(stepsReq2[step]) == 0:
                            stepsToRemove.append(step)
                            noReqs.append(step)
    print('workers = ' + str(workers))
    print('currentSteps = ' + str(currentSteps))
    print('done = ' + str(done))

    if len(stepsToRemove) > 0:
        for removed in stepsToRemove:
            if removed in stepsReq2:
                del stepsReq2[removed]

    currentSecond += 1


print('Total number of seconds = ' + str(currentSecond))
print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')
print()