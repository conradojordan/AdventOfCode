## Significantly faster solution for part 2 of day 1

# Saves initial time for execution time computing
import time
startTime = time.time()

# Opens input file and saves frequency changes in a list
file = open('input.txt')
frequencyChanges = file.read()
file.close()
frequencyChangesList = map(int, frequencyChanges.split())

# Variables initialization
shift = 0
frequencyList = [shift]
freqRepetitions = []

# Creates frequencies list using frequency changes list
for freqChange in frequencyChangesList:
        shift += freqChange
        frequencyList.append(shift)
del frequencyList[-1]

# Creates a list of frequency repetitions
for indexTarget in range(len(frequencyList)):
    for indexSource in range(len(frequencyList)):
        if (indexTarget == indexSource):
            continue
        deltaElements = frequencyList[indexTarget] - frequencyList[indexSource]
        if (deltaElements % shift == 0 and (deltaElements / shift > 0)):
            freqRepetitions.append([indexSource, int(deltaElements / shift), indexTarget])

# Checks if list of repetitions is empty. If not, saves the first repetition of all
if (len(freqRepetitions) == 0):
    print('No frequency ever repeats')
else:
    firstRepetition = freqRepetitions[0]
    for repetition in freqRepetitions:
        if (repetition[1] < firstRepetition[1]):
            firstRepetition = repetition
        elif (repetition[1] == firstRepetition[1] and repetition[0] < firstRepetition[0]):
            firstRepetition = repetition
    print('First repeated frequency: ' + str(frequencyList[firstRepetition[0]] + firstRepetition[1]*shift))

# Execution time of the program
print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')
