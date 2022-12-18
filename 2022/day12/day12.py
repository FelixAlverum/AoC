import sys


class distance:
    endnode = None
    distance = sys.maxsize

    def __int__(self, endnode, distance):
        self.endnode = endnode
        self.distance = distance


class node:
    value = '.'
    x = -1
    y = -1
    distances = []
    prevNode = None

    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def __init__(self, value, x, y, prevNode):
        self.value = value
        self.x = x
        self.y = y
        self.prevNode = prevNode


def loadData():
    heightmap = []
    with open('bspData.txt', 'r') as f:
        for x, line in enumerate(f):
            line = line.replace('\n', '')
            heightmap.append([])
            for y, char in enumerate(line):
                heightmap[x].append(char)
    return heightmap


def findUniquePos(heightmap, uniqueChar):
    for x, line in enumerate(heightmap):
        for y, c in enumerate(line):
            if c == uniqueChar:
                return [x, y]


def createNodeMap(heightmap, startnode, visitedNodes, unvisitedNodes):
    #set all possible distances to other nodes
    #1. Node above startnode
    if startnode.y - 1 > - 1:
        print('node above available')
        sv = ord(heightmap[startnode.x][startnode.y])
        na = ord(heightmap[startnode.x][startnode.y-1])

        if sv + 1 == na | sv == na | sv-1 == na:
            unvisitedNode = node(startnode.value+1, startnode.x, startnode.y-1, startnode)
            startnode.distances.append(distance(unvisitedNode,1))
    #2. Node right to startnode
    if startnode.x + 1 < len(heightmap[startnode.x]):
        print('node to the right available')
    #3. Node below startnode
    if startnode.y + 1 < len(heightmap):
        print('node below available')
    #4. Node left to startnode
    if startnode.x - 1 > -1:
        print('node to the left available')

    #add node to already visited nodes
    visitedNodes.append(startnode)


def removeUnvisitedNodeEntry(unvisitedNodes,x,y):
    for node in unvisitedNodes:
        if node.x == x & node.y == y:
            return unvisitedNodes.remove(node)

if __name__ == '__main__':
    heightmap = loadData()

    start = findUniquePos(heightmap, 'S')
    end = findUniquePos(heightmap, 'E')
    print(f'start: {start}, end: {end}')

    startnode = node(0, start[0], start[1])
    visitedNodes = []
    unvisitedNodes = []
    nodemap = createNodeMap(heightmap, startnode, visitedNodes, unvisitedNodes)