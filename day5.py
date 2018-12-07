import time
startTime = time.time()

# Opens file and reads polymer
file = open('input.txt')
originalPolymer = file.read().strip()
file.close()

# Function that makes all reactions in a polymer and return reduced polymer
def reducePolymer(polymer):
    reacted = True
    while (reacted and len(polymer) > 1):
        reacted = False
        reducedPolymer = ''
        combined = 0
        for i in range(len(polymer)-1):
            if (combined == 1):
                combined = 0
            elif (abs(ord(polymer[i]) - ord(polymer[i+1])) != 32):
                reducedPolymer += polymer[i]
            else:
                combined = 1
                reacted = True
        if (not combined):
            reducedPolymer += polymer[-1]
        polymer = reducedPolymer
    return reducedPolymer

# Function that removes all instances of a unit in a polymer
def removeUnit(polymer, badUnit):
    goodPolymer = ''
    for unit in polymer:
        if unit.lower() != badUnit.lower():
            goodPolymer += unit
    return goodPolymer


print('---- Program start ----')

## PART 1
print('Length polymer: ' + str(len(originalPolymer)) )
reduced = reducePolymer(originalPolymer)
print('Length reduced polymer: ' + str(len(reduced)) )

## PART 2
perUnitReduction = {}
for unit in 'abcdefghijklmnopqrstuvwxyz':
    noUnitPolymer = removeUnit(reduced, unit)
    noUnitReduced = reducePolymer(noUnitPolymer)
    perUnitReduction[unit] = len(noUnitReduced)

mostReduced = len(originalPolymer)
for unit in perUnitReduction:
    if (perUnitReduction[unit] < mostReduced):
        bestUnit = unit
        mostReduced = perUnitReduction[unit]

print('Best unit to remove = ' + bestUnit)
print('Length of polymer after unit removal and reduction = ' + str(mostReduced))
print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')
