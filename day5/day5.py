storage = [
    ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
    ['L', 'D', 'Z', 'Q', 'W', 'V'],
    ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
    ['Z', 'W', 'L', 'C'],
    ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
    ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
    ['D', 'P', 'J'],
    ['D', 'C', 'N', 'W', 'V']
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
        print(move)

if __name__ == '__main__':
    # Part 1
    moveCrates(loadData())

    # Part 2