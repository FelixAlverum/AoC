import math


def loadData():
    movement = []
    with open('Data.txt', 'r') as f:
        for line in f:
            movement.append(line.replace('\n', '').split(' '))
    return movement

def moveRope(movement):
    tailPath = [[0,0]] # unique coordinates from tail
    head = [0, 0]      # row = 0; col = 0
    tail = [0, 0]      # row = 0; col = 0

    for move in movement:
        if move[0] == 'U':      # UP
            for i in range(0, int(move[1]), 1):
                print(f'{i+1}. move {move}')
                # move head
                head[0] = head[0] + 1

                # check if tail has to move
                print(f'delta row {head[0]} -> {tail[0]} = {int(math.dist((head[0],), (tail[0],)))}\n'
                      f'delta col {head[1]} -> {tail[1]} = {int(math.dist((head[1],), (tail[1],)))}')
                if (int(math.dist((head[0],), (tail[0],))) < 2) & (int(math.dist((head[1],), (tail[1],))) < 2):
                    print('Do nothing')
                    continue    # do nothing head still touches tail

                # move tail
                tail[0] = tail[0] + 1       # tail go straight up
                if head[1] > tail[1]:
                    tail[1] = tail[1] + 1   # tail go diagonal right
                elif head[1] < tail[1]:
                    tail[1] = tail[1] - 1   # tail go diagonal left

                if [tail[0], tail[1]] not in tailPath:
                    tailPath.append([tail[0], tail[1]])

        if move[0] == 'D':      # Down
            for i in range(0, int(move[1]), 1):
                print(f'{i+1}. move {move}')
                # move head
                head[0] = head[0] - 1

                # check if tail has to move
                print(f'delta row {head[0]} -> {tail[0]} = {int(math.dist((head[0],), (tail[0],)))}\n'
                      f'delta col {head[1]} -> {tail[1]} = {int(math.dist((head[1],), (tail[1],)))}')
                if (int(math.dist((head[0],), (tail[0],))) < 2) & (int(math.dist((head[1],), (tail[1],))) < 2):
                    print('Do nothing')
                    continue    # do nothing head still touches tail

                # move tail
                tail[0] = tail[0] - 1       # tail go straight down
                if head[1] > tail[1]:
                    tail[1] = tail[1] + 1   # tail go diagonal right
                elif head[1] < tail[1]:
                    tail[1] = tail[1] - 1   # tail go diagonal left

                if [tail[0], tail[1]] not in tailPath:
                    tailPath.append([tail[0], tail[1]])

        if move[0] == 'L':      # Left
            for i in range(0, int(move[1]), 1):
                print(f'{i+1}. move {move}')
                # move head
                head[1] = head[1] - 1

                # check if tail has to move
                print(f'delta row {head[0]} -> {tail[0]} = {int(math.dist((head[0],), (tail[0],)))}\n'
                      f'delta col {head[1]} -> {tail[1]} = {int(math.dist((head[1],), (tail[1],)))}')
                if (int(math.dist((head[0],), (tail[0],))) < 2) & (int(math.dist((head[1],), (tail[1],))) < 2):
                    print('Do nothing')
                    continue    # do nothing head still touches tail

                # move tail
                tail[1] = tail[1] - 1       # tail go straight left
                if head[0] > tail[0]:
                    tail[0] = tail[0] + 1   # tail go diagonal up
                elif head[0] < tail[0]:
                    tail[0] = tail[0] - 1   # tail go diagonal down

                if [tail[0], tail[1]] not in tailPath:
                    tailPath.append([tail[0], tail[1]])

        if move[0] == 'R':      # Right
            for i in range(0, int(move[1]), 1):
                print(f'{i+1}. move {move}')
                # move head
                head[1] = head[1] + 1

                # check if tail has to move
                print(f'delta row {head[0]} -> {tail[0]} = {int(math.dist((head[0],), (tail[0],)))}\n'
                      f'delta col {head[1]} -> {tail[1]} = {int(math.dist((head[1],), (tail[1],)))}')
                if (int(math.dist((head[0],), (tail[0],))) < 2) & (int(math.dist((head[1],), (tail[1],))) < 2):
                    print('Do nothing')
                    continue    # do nothing head still touches tail

                # move tail
                tail[1] = tail[1] + 1       # tail go straight right
                if head[0] > tail[0]:
                    tail[0] = tail[0] + 1   # tail go diagonal up
                elif head[0] < tail[0]:
                    tail[0] = tail[0] - 1   # tail go diagonal down

                if [tail[0], tail[1]] not in tailPath:
                    tailPath.append([tail[0], tail[1]])
    print(len(tailPath))

def getMovementCoordinates(movement):
    headPath = [[0,0]] # coordinates from tail
    head = [0, 0]      # row = 0; col = 0

    for move in movement:
        if move[0] == 'U':      # UP
            for i in range(0, int(move[1]), 1):
                # move head
                head[0] = head[0] + 1
                headPath.append([head[0], head[1]])

        if move[0] == 'D':      # Down
            for i in range(0, int(move[1]), 1):
                # move head
                head[0] = head[0] - 1
                headPath.append([head[0], head[1]])

        if move[0] == 'L':      # Left
            for i in range(0, int(move[1]), 1):
                # move head
                head[1] = head[1] - 1
                headPath.append([head[0], head[1]])

        if move[0] == 'R':      # Right
            for i in range(0, int(move[1]), 1):
                # move head
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

        #up
        if cordinate[0] > tail[0]:
            tail[0] = tail[0] + 1  # tail go straight up
            if cordinate[1] > tail[1]:
                tail[1] = tail[1] + 1  # tail go diagonal right
            elif cordinate[1] < tail[1]:
                tail[1] = tail[1] - 1  # tail go diagonal left
            tailPath.append([tail[0], tail[1]])
            continue

        #down
        if cordinate[0] < tail[0]:
            tail[0] = tail[0] - 1  # tail go straight down
            if cordinate[1] > tail[1]:
                tail[1] = tail[1] + 1  # tail go diagonal right
            elif cordinate[1] < tail[1]:
                tail[1] = tail[1] - 1  # tail go diagonal left
            tailPath.append([tail[0], tail[1]])
            continue

        #left
        if cordinate[1] < tail[1]:
            tail[1] = tail[1] - 1  # tail go straight left
            if cordinate[0] > tail[0]:
                tail[0] = tail[0] + 1  # tail go diagonal up
            elif cordinate[0] < tail[0]:
                tail[0] = tail[0] - 1  # tail go diagonal down
            tailPath.append([tail[0], tail[1]])
            continue

        # right
        if cordinate[1] > tail[1]:
            tail[1] = tail[1] + 1  # tail go straight right
            if cordinate[0] > tail[0]:
                tail[0] = tail[0] + 1  # tail go diagonal up
            elif cordinate[0] < tail[0]:
                tail[0] = tail[0] - 1  # tail go diagonal down
            tailPath.append([tail[0], tail[1]])

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

    for row in range(0,offsetRow*2,1):
        for col in range(0,offsetCol*2,1):
            print(grid[row][col] , end= '')
        print()

if __name__ == '__main__':
    movement = loadData()

    # Part 1
    #moveRope(movement)

    # Part 2
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

    #print(f'len(t9) {len(t9)} , t9 {t9}')

    uniqueCords = []
    for cord in t9:
        if cord not in uniqueCords:
            uniqueCords.append(cord)
    print(len(uniqueCords))

    #printCoords(t9) für Testdaten