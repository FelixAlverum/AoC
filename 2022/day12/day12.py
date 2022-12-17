def loadData():
    heightmap = []
    with open('data.txt', 'r') as f:
        for i, line in enumerate(f):
            line = line.replace('\n','')
            heightmap.append([])
            for char in line:
               heightmap[i].append(char)
    return heightmap

if __name__ == '__main__':
    heightmap = loadData()

    for line in heightmap:
        for c in line:
            print(c, end='')
        print()