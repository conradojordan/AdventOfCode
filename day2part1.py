# Opens file and saves box IDs in a list
file = open('input.txt')
idList = file.read().split()
file.close()

frequencies = {2: 0, 3: 0}

# For each box ID, checks if it has a letter that appears twice
# and/or a letter that appears thrice
for boxId in idList:
    twoLetters = False
    threeLetters = False
    for letter in boxId:
        letterCount = boxId.count(letter)
        if (letterCount == 2):
            twoLetters = True
        if (letterCount == 3):
            threeLetters = True
    # Increments number of IDs with two and/or three letter repetitions if necessary
    if (twoLetters):
        frequencies[2] += 1
    if (threeLetters):
        frequencies[3] += 1

# Prints the checksum
print(frequencies[2]*frequencies[3])
