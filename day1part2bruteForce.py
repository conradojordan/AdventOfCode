import time
startTime = time.time()
file = open('input.txt')
frequencyChanges = file.read()
frequencyChangesList = map(int, frequencyChanges.split())

currentFrequency = 0
frequencyList = [currentFrequency]
foundDuplicate = 0
iteration = 0
while (not foundDuplicate):
    iteration += 1
    for freqChange in frequencyChangesList:
        currentFrequency += freqChange
        if (currentFrequency in frequencyList):
            foundDuplicate = 1
            firstDuplicateFrequency = currentFrequency
            frequencyList.append(currentFrequency)
            break
        frequencyList.append(currentFrequency)
    currentFrequency
    print('Iteration ' + str(iteration))
    print('currentFrequency = ' + str(currentFrequency))
print('First repeated frequency: ' + str(firstDuplicateFrequency))
print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')
