# Opens the input file and save the frequency changes in a list
file = open('input.txt')
frequencyChanges = file.read()
file.close()
frequencyChangesList = map(int, frequencyChanges.split())

# Sums and subtracts the frequency changes until reaching the last frequency
currentFrequency = 0
for freqChange in frequencyChangesList:
    currentFrequency += freqChange
print(currentFrequency)
