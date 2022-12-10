import math


def loadData():
    movement = []
    with open('bspData.txt', 'r') as f:
        for line in f:
            movement.append(line.replace('\n', '').split(' '))
    return movement

def getMovementCoordinates(movement):
    headPath = [[0,0]] # coordinates from tail
    head = [0, 0]      # row = 0; col = 0

    for move in movement:
        if move[0] == 'U':      # UP
            for i in range(0, int(move[1]), 1):
                head[0] = head[0] + 1
                headPath.append([head[0], head[1]])

        if move[0] == 'D':      # Down
            for i in range(0, int(move[1]), 1):
                head[0] = head[0] - 1
                headPath.append([head[0], head[1]])

        if move[0] == 'L':      # Left
            for i in range(0, int(move[1]), 1):
                head[1] = head[1] - 1
                headPath.append([head[0], head[1]])

        if move[0] == 'R':      # Right
            for i in range(0, int(move[1]), 1):
                head[1] = head[1] + 1
                headPath.append([head[0], head[1]])
    return headPath

def moveRopeByCoordinates(cordinatesMovement):
    tailPath = [[0, 0]]     # coordinates from tail
    tail = [0, 0]           # row = 0; col = 0

    for cordinate in cordinatesMovement:
        #cordinate = head

        # check if tail has to move
        if (int(math.dist((cordinate[0],), (tail[0],))) < 2) & (int(math.dist((cordinate[1],), (tail[1],))) < 2):
            continue  # do nothing head still touches tail

        #up or down
        if (cordinate[0] > tail[0]) | (cordinate[0] < tail[0]):
            if (cordinate[0] > tail[0]):
                tail[0] = tail[0] + 1  #up
            else:
                tail[0] = tail[0] - 1  # down

            if cordinate[1] > tail[1]:
                tail[1] = tail[1] + 1  # tail go diagonal right
            elif cordinate[1] < tail[1]:
                tail[1] = tail[1] - 1  # tail go diagonal left
            tailPath.append([tail[0], tail[1]])
            continue

        #left or right
        if (cordinate[1] < tail[1]) | (cordinate[1] > tail[1]):
            if (cordinate[1] < tail[1]):
                tail[1] = tail[1] - 1  # left
            else:
                tail[1] = tail[1] + 1  # right

            if cordinate[0] > tail[0]:
                tail[0] = tail[0] + 1  # tail go diagonal up
            elif cordinate[0] < tail[0]:
                tail[0] = tail[0] - 1  # tail go diagonal down
            tailPath.append([tail[0], tail[1]])
            continue

    return tailPath

def printCoords(cords):
    grid = []
    offsetRow = 20
    offsetCol = 30

    for row in range(0,offsetRow*2,1):
        grid.append([])
        for col in range(0,offsetCol*2,1):
            grid[row].append('.')

    for cord in cords:
        grid[cord[0]+offsetRow][cord[1]+offsetCol] = '#'

    for row in reversed(range(0,offsetRow*2,1)):
        for col in range(0,offsetCol*2,1):
            print(grid[row][col] , end= '')
        print()

def getUniqueCords(cords):
    uniqueCords = []
    for cord in cords:
        if cord not in uniqueCords:
            uniqueCords.append(cord)
    return len(uniqueCords)


if __name__ == '__main__':
    movement = loadData()

    head = getMovementCoordinates(movement)
    t1 = moveRopeByCoordinates(head)
    t2 = moveRopeByCoordinates(t1)
    t3 = moveRopeByCoordinates(t2)
    t4 = moveRopeByCoordinates(t3)
    t5 = moveRopeByCoordinates(t4)
    t6 = moveRopeByCoordinates(t5)
    t7 = moveRopeByCoordinates(t6)
    t8 = moveRopeByCoordinates(t7)
    t9 = moveRopeByCoordinates(t8)

    # Part 1
    print(f'P1: {getUniqueCords(t1)}')

    # Part 2
    print(f'P2: {getUniqueCords(t9)}')

    printCoords(t9) # für Testdaten