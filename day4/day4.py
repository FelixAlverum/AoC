def loadData():
    shifts = []
    with open('data.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            shift = [
                int(line[:line.index('-')]),
                line[line.index('-'):line.index(',')],
                line[line.index(','):line.index('-')],      # TODO hier weiter machen
                line[:int(len(line) / 2)]
            ]
    return shifts

if __name__ == '__main__':
    # Part 1
    loadData()

    # Part 2