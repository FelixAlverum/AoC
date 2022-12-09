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



if __name__ == '__main__':
    movement = loadData()

    # Part 1
    moveRope(movement)


    # Part 2
