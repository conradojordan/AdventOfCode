import time
startTime = time.time()
file = open('input.txt')
frequencyChanges = file.read()
frequencyChangesList = map(int, frequencyChanges.split())

shift = 0
frequencyList = [shift]
freqRepetitions = []

for freqChange in frequencyChangesList:
        shift += freqChange
        frequencyList.append(shift)
del frequencyList[-1]

for indexTarget in range(len(frequencyList)):
    for indexSource in range(len(frequencyList)):
        if (indexTarget == indexSource):
            continue
        deltaElements = frequencyList[indexTarget] - frequencyList[indexSource]
        if (deltaElements % shift == 0 and (deltaElements / shift > 0)):
            freqRepetitions.append([indexSource, int(deltaElements / shift), indexTarget])

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
print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')
