import numpy as np
f = open('./input.txt', 'r')
data = []
for x in f:
    numbers = x.split(',')
    for i in numbers:
        data.append(int(i))

def spawnFishInterval(data):
    newData = []
    for i in range(len(data)):
        if (data[i] == 0):
            data[i] = 6
            newData.append(8)
        else:
            data[i]-=1
        newData.append(data[i])
    return newData

# Exercise 1
def exercise1():
    newData = data
    givenDays = 80
    counter = 0
    while (counter != givenDays):
        newData = spawnFishInterval(newData)
        counter+=1
    print(len(newData))

def initializeFishCounts():
    fishCounts=np.zeros(9)
    for i in range(len(data)):
        fishCounts[data[i]]+=1
    return fishCounts


# Exercise 2
<<<<<<< HEAD
=======

>>>>>>> 2db849d3ad07ad9e46acde9fe1d9d6be9cf2b662
def updateFishCount(fishCounts):
    newFishesCount = 0
    for i in range(len(fishCounts)):
        if (i == 0):
            newFishesCount+=fishCounts[i]
            fishCounts[i] = fishCounts[i + 1]
        else:
            fishCounts[i-1] = fishCounts[i]
    fishCounts[8] = newFishesCount
    fishCounts[6] = fishCounts[6] + newFishesCount
    return fishCounts

def exercise2():
    fishCounts = initializeFishCounts()
    givenDays = 256
    counter = 0
    while (counter != givenDays):
        fishCounts = updateFishCount(fishCounts)
        counter+=1
    print(np.sum(fishCounts))

exercise1()
exercise2()