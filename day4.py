import re

# Opens file and saves records in a list
file = open('input.txt')
allRecords = file.read()
file.close()
records = allRecords.strip().split('\n')

records.sort()

guardMinutes = {}
guardNumRegex = re.compile(r'#(\d+)')
asleepRegex = re.compile(r'falls asleep')

# Creating dictionary
# guardMinutes { guard1: {minute1: times, minute2:times}, guard2: {minute1: times} }

for record in records:
    guardNum = guardNumRegex.findall(record)
    asleep = asleepRegex.findall(record)
    if (len(guardNum) == 1):
        currentGuard = int(guardNum[0])
    elif (len(asleep) == 1):
        startTime = int(record[15:17])
    else:
        finishTime = int(record[15:17])
        guardMinutes.setdefault(currentGuard, {})
        for minute in range(startTime, finishTime):
            guardMinutes[currentGuard].setdefault(minute,0)
            guardMinutes[currentGuard][minute] += 1

# Find guard that most sleeps
mostMinutes = 0
for guard in guardMinutes:
    if (sum(guardMinutes[guard].values()) > mostMinutes):
        mostMinutes = sum(guardMinutes[guard].values())
        sleepyGuard = guard

# Find minute most slept
mostTimes = 0
for minuteAndTimes in guardMinutes[sleepyGuard].items():
    if (minuteAndTimes[1] > mostTimes):
        mostTimes = minuteAndTimes[1]
        sleepyMinute =  minuteAndTimes[0]

print('--- First strategy ---')
print('Sleepy guard = ' + str(sleepyGuard))
print('Sleepy minute = ' + str(sleepyMinute) + ' (slept ' + str(mostTimes) + ' times)')
print('Sleepy guard x sleepy minute = ' + str(sleepyGuard*sleepyMinute))


## PART 2
# Find most slept minute of all guards
mostTimes2 = 0
for guard in guardMinutes:
    for minuteAndTimes in guardMinutes[guard].items():
        if (minuteAndTimes[1] > mostTimes2):
            mostTimes2 = minuteAndTimes[1]
            sleepyMinute2 =  minuteAndTimes[0]
            sleepyGuard2 = guard

print('\n--- Second strategy ---')
print('Sleepy guard 2 = ' + str(sleepyGuard2))
print('Sleepy minute 2 = ' + str(sleepyMinute2) + ' (slept ' + str(mostTimes2) + ' times)')
print('Sleepy guard 2 x sleepy minute 2 = ' + str(sleepyGuard2*sleepyMinute2))
