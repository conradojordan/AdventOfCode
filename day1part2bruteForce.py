## Brute force solution for part 2 of day 1

# Saves initial time for execution time computing
import time
startTime = time.time()

# Opens input file and saves frequency changes in a list
file = open('input.txt')
frequencyChanges = file.read()
file.close()
frequencyChangesList = map(int, frequencyChanges.split())

# Variables initialization
currentFrequency = 0
frequencyList = [currentFrequency]
foundDuplicate = 0
iteration = 0

# Keeps saving all reached frequencies and checking if a frequency has already been reached before
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
    
    # Prints current iteration
    print('Iteration ' + str(iteration))

# Solution and execution time of the program
print('First repeated frequency: ' + str(firstDuplicateFrequency))
print('Program execution time: ' + str(round(time.time() - startTime, 3)) + ' seconds')
