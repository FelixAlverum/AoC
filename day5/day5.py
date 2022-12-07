storage = [
    ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],   #0
    ['L', 'D', 'Z', 'Q', 'W', 'V'],             #1
    ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],   #2
    ['R', 'D', 'H', 'F', 'J', 'V', 'B'],        #3
    ['Z', 'W', 'L', 'C'],                       #4
    ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],   #5
    ['J', 'R', 'L', 'V', 'M', 'B', 'S'],        #6
    ['D', 'P', 'J'],                            #7
    ['D', 'C', 'N', 'W', 'V']                   #8
]

def loadData():
    movement = []
    with open('data.txt', 'r') as f:
        ctr = 1
        for line in f:
            line = line.replace('\n', '')
            ctr = ctr + 1
            if ctr < 12:
                continue
            details = [
                int(line[5:line.index(' from ')]),                     # how many crates to move
                int(line[line.index('from') + 5:line.find(' to ')]),   # From
                int(line[line.find(' to ') + 4:])                      # To
            ]
            movement.append(details)
    return movement

def moveCrates(movement):
    for move in movement:
        #print(move)
        stFrom = move[1]-1                                  # starts counting at 1 --> -1 so its the same as index
        stTo = move[2]-1                                    # starts counting at 1 --> -1 so its the same as index
        indexAmount = len(storage[stFrom])-move[0]
        #print(f'stFrom {stFrom}')
        #print(f'Storage FROM before {storage[stFrom]}')
        crane = storage[stFrom][indexAmount:]               # load crane
        storage[stFrom] = storage[stFrom][:indexAmount]     # leave rest on storage
        #print(f'Crane Loaded {crane}')
        #print(f'Storage FROM after {storage[stFrom]}')
        #print(f'Storage TO before {storage[stTo]}')
        for unit in reversed(crane):
            storage[stTo].append(unit)
        #print(f'Storage TO after {storage[stTo]}')

    for storageUnit in storage:
        print(f'Part 1 {storageUnit[len(storageUnit) - 1]}')


def moveCrates2(movement):
    for move in movement:
        print(move)
        stFrom = move[1]-1                                  # starts counting at 1 --> -1 so its the same as index
        stTo = move[2]-1                                    # starts counting at 1 --> -1 so its the same as index
        indexAmount = len(storage[stFrom])-move[0]
        print(f'stFrom {stFrom}')
        print(f'Storage FROM before {storage[stFrom]}')
        crane = storage[stFrom][indexAmount:]               # load crane
        storage[stFrom] = storage[stFrom][:indexAmount]     # leave rest on storage
        print(f'Crane Loaded {crane}')
        print(f'Storage FROM after {storage[stFrom]}')
        print(f'Storage TO before {storage[stTo]}')
        for unit in crane:
            storage[stTo].append(unit)
        print(f'Storage TO after {storage[stTo]}')

    for storageUnit in storage:
        print(f'Part 2 {storageUnit[len(storageUnit) - 1]}')

if __name__ == '__main__':
    # Part 1
    # moveCrates(loadData())

    # Part 2
    moveCrates2(loadData())