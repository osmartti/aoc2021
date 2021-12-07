f = open('./input.txt', 'r')
data = []
for x in f:
    numbers = x.split(',')
    for i in numbers:
        data.append(int(i))

def getInitialPositions():
    positions = dict()
    for i in range(min(data), max(data)+1):
        positions[i] = 0
    for i in range(len(data)):
        positions[data[i]]+=1
    return positions

def calculateBestPosition(positions):
    sums = dict()
    for i in range(len(positions.keys())):
        fuelConsumption = 0
        for key, value in positions.items():
            fuelConsumption = fuelConsumption + value * abs(i - key)
        sums[i] = fuelConsumption
    result = min(sums.values())
    return result

def calculatePositionCost(index):
    fuelConsumption = 0
    for i in range(len(data)):
        numberOfSteps = abs(data[i] - index)
        n=numberOfSteps/2+0.5
        fuelConsumption += n*numberOfSteps
    return fuelConsumption

# Exercise 1
def exercise1():
    initialPositions = getInitialPositions()
    result = calculateBestPosition(initialPositions)
    print(result)

# Exercise 2
def exercise2():
    best = float('inf')
    for i in range(max(data)+1):
        result = calculatePositionCost(i)
        if (result < best):
            best = result
    print(best)

exercise1()
exercise2()