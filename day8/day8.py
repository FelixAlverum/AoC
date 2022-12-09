def loadData():
    data = []
    with open('Data.txt', 'r') as f:
        for line in f:
            data.append(line.replace('\n', ''))
            print(line.replace('\n', ''))
    return data


if __name__ == '__main__':
    loadData()

    # Part 1

    # Part 2

