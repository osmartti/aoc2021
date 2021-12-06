import numpy as np

f = open('./input.txt', 'r')
data = []
for x in f:
    line = x.strip()
    numbers = line.split(' -> ')
    cordinates=[]
    for i in range(len(numbers)):
        values = numbers[i].split(',')
        for j in range(len(values)):
            cordinates.append(int(values[j]))
    data.append(cordinates)

def createGrid(data):
    gridMaxX = 0
    gridMaxY = 0
    for i in range(len(data)):
        for j in range(len(data[i])):    
            currentX = int(data[i][j])
            currentY = int(data[i][j])
            if (currentX > gridMaxX):
                gridMaxX = currentX
            if (currentY > gridMaxY):
                gridMaxY = currentY
    # Create np array here with grid max and min
    arr = np.full((gridMaxX + 1, gridMaxY + 1), 0)
    return arr

# Exercise one
def exerciseOne():
    grid = createGrid(data)
    resultCount = 0
    for i in range(len(data)):
        fromX = data[i][0]
        fromY = data[i][1]
        toX = data[i][2]
        toY = data[i][3]
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if ((fromX <= x <= toX and fromY <= y <= toY) or (fromX >= x >= toX and fromY >= y >= toY)):
                    if (fromX == toX or fromY == toY):
                        grid[y][x]+= 1
                        if (grid[y][x] == 2):
                            resultCount+=1
    print(resultCount)

exerciseOne()