file = open('input.txt')
frequencyChanges = file.read()
frequencyChangesList = map(int, frequencyChanges.split())

currentFrequency = 0
for freqChange in frequencyChangesList:
    currentFrequency += freqChange
print(currentFrequency)
