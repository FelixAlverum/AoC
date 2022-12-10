import string


def loadData():
    backpacks = []
    with open('data.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            backpack = [line[:int(len(line) / 2)], line[int(len(line) / 2):]]
            backpacks.append(backpack)
    return backpacks


def findItem(backpacks):
    items = []

    for backpack in backpacks:
        for item1 in backpack[0]:
            if item1 in backpack[1]:
                items.append(item1)
                break
    return items


def calcPrio(items, part):
    priorities = []
    sumPrio= 0

    for abc in (string.ascii_lowercase + string.ascii_uppercase):
        priorities.append(abc)

    for i in items:
        sumPrio = sumPrio + priorities.index(i) + 1

    print(f'Part {part}: {sumPrio}')


def loadDataP2():
    backpacks = []
    backpack = []
    ctr = 0
    with open('data.txt', 'r') as f:
        for line in f:
            ctr = ctr + 1
            backpack.append(line.replace('\n', ''))
            if ctr == 3:
                backpacks.append(backpack)
                backpack = []
                ctr = 0
    return backpacks


def findItem2(backpacks):
    items = []
    ctr = 0

    for backpack in backpacks:
        for item1 in backpack[0]:
            if (item1 in backpack[1]) & (item1 in backpack[2]):
                items.append(item1)
                ctr = ctr + 1
                break
    return items


if __name__ == '__main__':
    # Part 1
    calcPrio(findItem(loadData()),1)

    # Part 2
    calcPrio(findItem2(loadDataP2()),2)