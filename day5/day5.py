def loadData():
    movement = []
    with open('data.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            movement.append(line)
            print(line)
    return movement

if __name__ == '__main__':
    # Part 1
    loadData()

    # Part 2