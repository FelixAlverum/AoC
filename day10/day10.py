def loadData():
    instructions = []
    with open('Data.txt', 'r') as f:
        for line in f:
            if line == 'noop':
                instructions.append([line.replace('\n', '')])         #noop
            else:
                instructions.append(line.replace('\n', '').split(' '))      #addx
    return instructions

def executeInstructions(instructions):
    cycle = 0
    signalStrength = 0
    registerValue = 1

    for op in instructions:
        if op[0] == 'noop':
            cycle = cycle + 1
            signalStrength = evaluateCycle(cycle, signalStrength, registerValue)
        else:
            cycle = cycle + 1
            signalStrength = evaluateCycle(cycle, signalStrength, registerValue)
            cycle = cycle + 1
            signalStrength = evaluateCycle(cycle, signalStrength, registerValue)
            registerValue = registerValue + int(op[1])
    print(f'sum signalStrength {signalStrength}')

def evaluateCycle(cycle, signalStrength, registerValue):
    if not (cycle+20) % 40 == 0:
        return signalStrength

    signalStrength = signalStrength + cycle * registerValue
    #print(f'cycle {cycle} register {registerValue} signalstrength {cycle * registerValue}')
    return signalStrength

def drawSprite(instructions):
    cycle = -1
    registerValue = 1
    grid = []
    spritePosition = [0, 1, 2]

    # Create empty Monitor ('.')
    for row in range(0, 6, 1):
        grid.append([])
        for col in range(0, 40, 1):
            grid[row].append('.')

    # Add Pixels ('#') on monitor
    for op in instructions:
        if op[0] == 'noop':
            cycle = cycle + 1
            if cycle % 40 in spritePosition:
                grid[cycle // 40][cycle % 40] = '#'
        else:
            cycle = cycle + 1
            if cycle % 40 in spritePosition:
                grid[cycle // 40][cycle % 40] = '#'

            cycle = cycle + 1
            if cycle % 40 in spritePosition:
                grid[cycle // 40][cycle % 40] = '#'

            # move sprite
            registerValue = registerValue + int(op[1])
            spritePosition = [registerValue-1, registerValue + 0, registerValue + 1]

    # Print Monitor
    for row in range(0,6,1):
        for col in range(0,40,1):
            print(grid[row][col], end='')
        print()


if __name__ == '__main__':
    instructions = loadData()

    # Part 1
    executeInstructions(instructions)

    # Part 2
    drawSprite(instructions)
