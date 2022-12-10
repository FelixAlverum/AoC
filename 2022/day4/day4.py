def loadData():
    shifts = []
    with open('data.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            shift = [
                int(line[:line.index('-')]),
                int(line[line.index('-')+1:line.index(',')]),
                int(line[line.index(',')+1:line.find('-', line.index(','))]),
                int(line[line.find('-', line.index(','))+1:])
            ]
            shifts.append(shift)
    return shifts

def countInboundShifts(shifts):
    inboundShifts = 0
    for shift in shifts:
        if (shift[0] <= shift[2]) & (shift[1] >= shift[3]) | (shift[2] <= shift[0]) & (shift[3] >= shift[1]):
            inboundShifts = inboundShifts + 1
    print(f'P1: {inboundShifts}')

def countRangeShifts(shifts):
    rangeShifts = 0
    for shift in shifts:
        if (shift[0] <= shift[2]) & (shift[1] >= shift[2]) | (shift[2] <= shift[0]) & (shift[3] >= shift[0]):
            rangeShifts = rangeShifts + 1

    print(f'P2: {rangeShifts}')

if __name__ == '__main__':
    # Part 1
    countInboundShifts(loadData())

    # Part 2
    countRangeShifts(loadData())