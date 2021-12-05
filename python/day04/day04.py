f = open('./input.txt', 'r')
data = []
for x in f:
    line = x.strip()
    if (len(line) != 0):
        data.append(line)
bingoNumbers = data[0].split(',')
del data[0]

def modifyRowData(row):
    newRow = row.replace('  ', ' ')
    newRow = newRow.replace(' ', ',')
    return newRow

# Create bingobooks/boards
bingoCounter = 0
newData = []
newBingoBook = []
for i in range(len(data)):
    newBingoBook.append(modifyRowData(data[i]))
    bingoCounter += 1
    if (bingoCounter == 5):
        newData.append(newBingoBook)
        newBingoBook = []
        bingoCounter = 0

def markRowNumber(row, number):
    rowNumbers = row.split(',')
    for i in range(len(rowNumbers)):
        if (rowNumbers[i] == number):
            rowNumbers[i] = rowNumbers[i] + 'm'
    return ','.join(rowNumbers)

def checkIfBingoBoardWon(board):
    foundScores = []
    for i in range(len(board)):
        rowNumbers = board[i].split(',')
        for j in range(len(rowNumbers)):
            if ('m' in rowNumbers[j]):
                foundScores.append([int(i), int(j)])
    xCords = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    yCords = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for i in range(len(foundScores)):
        for j in range(len(foundScores[i])):
            if (j == 0):
                xCords[foundScores[i][j]] += 1
            else:  
                yCords[foundScores[i][j]] += 1
    if (any(v == 5 for v in iter(xCords.values()))):
        return True
    elif (any(v == 5 for v in iter(yCords.values()))):
        return True
    else:
        return False

def calculateUnmarkedScores(board):
    unmarkedNumbers = []
    unmarkedSum = 0
    for i in range(len(board)):
        rowNums = board[i].split(',')
        for j in range(len(rowNums)):
            if ('m' not in rowNums[j]):
                unmarkedNumbers.append(int(rowNums[j]))
    for i in unmarkedNumbers:
        unmarkedSum += i
    return unmarkedSum

# Exercise 1
def exercise1():
    markedNumbers = []
    winningBoard = []
    for i in range(len(bingoNumbers)):
        if (len(winningBoard) != 0):
            break 
        currentNumber = bingoNumbers[i]
        markedNumbers.append(currentNumber)
        for j in range(len(newData)):
            bingoBoard = newData[j]
            for z in range(len(bingoBoard)):
                currentRow = bingoBoard[z]
                newRow = markRowNumber(currentRow, currentNumber)
                bingoBoard[z] = newRow
            if (checkIfBingoBoardWon(bingoBoard)):
                winningBoard = bingoBoard
                break 
    unmarkedScoresSum = calculateUnmarkedScores(winningBoard)
    lastCalledNumber = int(markedNumbers[len(markedNumbers) - 1])
    print(unmarkedScoresSum * lastCalledNumber)

def boardNotYetWon(boardIndex, winningBoards):
    if (len(winningBoards) == 0):
        return True
    for i in range(len(winningBoards)):
        if (boardIndex in winningBoards[i]):
            return False
    return True

# Exercise 2
def exercise2():
    markedNumbers = []
    numberOfBoards = len(newData)
    winningBoards = []
    for i in range(len(bingoNumbers)):
        if (numberOfBoards == len(winningBoards)):
            break
        currentNumber = bingoNumbers[i]
        markedNumbers.append(currentNumber)
        for j in range(len(newData)):
            bingoBoard = newData[j]
            for z in range(len(bingoBoard)):
                currentRow = bingoBoard[z]
                newRow = markRowNumber(currentRow, currentNumber)
                bingoBoard[z] = newRow
            if(checkIfBingoBoardWon(bingoBoard)):
                if (boardNotYetWon(j, winningBoards)):
                    winningBoards.append({j: bingoBoard})
                if (numberOfBoards == len(winningBoards)):
                    break
    winningBoard = winningBoards[len(winningBoards) - 1]
    for v in winningBoard.values():
        winningBoard = v
    unmarkedScoresSum = calculateUnmarkedScores(winningBoard)
    lastCalledNumber = int(markedNumbers[len(markedNumbers) - 1])
    print(unmarkedScoresSum * lastCalledNumber)

exercise1()
exercise2()