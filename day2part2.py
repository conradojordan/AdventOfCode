# Opens file and saves box IDs in a list
file = open('input.txt')
idList = file.read().split()
file.close()

# Searches for box IDs with only 1 letter difference (and saves index of letter)
for firstBox in idList:
    for secondBox in idList:
        numDiff = 0
        i = 0
        while (numDiff < 2 and i < len(firstBox)):
            if (firstBox[i] is not secondBox[i]):
                indexDiff = i
                numDiff += 1
            i += 1
        if (numDiff == 1):
            break
    if(numDiff == 1):
        break

print('First box = ' + firstBox)
print('Second box = ' + secondBox)
inCommon = ''
for i in range(len(firstBox)):
    if (i is not indexDiff):
        inCommon += firstBox[i]
print('Letters in common = ' + inCommon)
