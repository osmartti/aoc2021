f = open('./input.txt', 'r')
data = []
for x in f:
    data.append(x.strip())

def binaryToDecimal(n):
    return int(n,2)

def getMostCommon(listData, index, measurement = None):
    mostCommon = -1
    binaryList = []
    for i in range(len(listData)):
        binaryList.append(listData[i][index])
    countZero = 0
    countOne = 0
    for i in range(len(binaryList)):
        if (binaryList[i] == '0'):
            countZero +=1
        else:    
            countOne +=1
    if (countZero > countOne):
        mostCommon = 1 if measurement == 'co2' else 0
    if (countOne > countZero):
        mostCommon = 0 if measurement == 'co2' else 1
    return mostCommon

# Exercise 1
gammaRate = epsilonRate = ''
for i in range(len(data[0])):
    mostCommon = getMostCommon(data, i)
    if (mostCommon == 0):
        gammaRate+='0'
        epsilonRate+='1'
    else:
        gammaRate+='1'
        epsilonRate+='0'
print(binaryToDecimal(gammaRate) * binaryToDecimal(epsilonRate))

# Exercise 2
def getLifeSupportRating(measurement):
    stringIndex = 0
    newList = data
    while len(newList) != 1:
        newList = returnBinaryList(newList, stringIndex, measurement)
        stringIndex +=1 
    return binaryToDecimal(newList[0])

def returnBinaryList(listData, stringIndex, measurement):
    newData = []
    if (measurement == 'oxygen'):
        measurementValue = getMostCommon(listData, stringIndex, 'oxygen')
    if (measurement == 'co2'):
        measurementValue = getMostCommon(listData, stringIndex, 'co2')
    for i in range(len(listData)):
        if (listData[i][stringIndex] == '1' and measurementValue == 1): 
            newData.append(listData[i])
        if (listData[i][stringIndex] == '0' and measurementValue == 0):
            newData.append(listData[i])
        if (measurementValue == -1):
            if (measurement == 'oxygen' and listData[i][stringIndex] == '1'):
                newData.append(listData[i])
            if (measurement == 'co2' and listData[i][stringIndex] == '0'):
                newData.append(listData[i])
    return newData
print(getLifeSupportRating('oxygen') * getLifeSupportRating('co2'))