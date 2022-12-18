import sys


class node:
    value = sys.maxsize
    x = -1
    y = -1
    prevNode = None

    # the distance to all adjacent nodes is 1 --> no distance variable needed

    def __init__(self, value, x, y, prevNode):
        self.value = value
        self.x = x
        self.y = y
        self.prevNode = prevNode

    def __eq__(self, other):
        if self.x == other.x & self.y == other.y:
            return True
        return False

    def __str__(self):
        if self.prevNode == None:
            str = f'value {self.value} --> x = {self.x}; y = {self.y} --- parent = self'
        else:
            str = f'value {self.value} --> x = {self.x}; y = {self.y} --- parent {self.prevNode.value}'
        return str


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
    unvisitedNodes.append(startnode)

    while len(unvisitedNodes) > 0:
        currentNode = unvisitedNodes[0]

        # 1. Node above currentNode
        if currentNode.x - 1 > - 1:
            unvisitedNodes = updateNode(heightmap, visitedNodes, unvisitedNodes, currentNode, 'up')

        # 2. Node right to currentNode
        if currentNode.y + 1 < len(heightmap[currentNode.x]):
            unvisitedNodes = updateNode(heightmap, visitedNodes, unvisitedNodes, currentNode, 'right')

        # 3. Node below currentNode
        if currentNode.x + 1 < len(heightmap):
            unvisitedNodes = updateNode(heightmap, visitedNodes, unvisitedNodes, currentNode, 'down')

        # 4. Node left to currentNode
        if currentNode.y - 1 > -1:
            unvisitedNodes = updateNode(heightmap, visitedNodes, unvisitedNodes, currentNode, 'left')

        unvisitedNodes = sorted(unvisitedNodes, key=lambda x: x.value)
        for i, un in enumerate(unvisitedNodes):
            if i == 0:
                print()
            print(f'{i+1} / {len(unvisitedNodes)} --- unvisited node: {un}')

        # add node to already visited nodes
        visitedNodes.append(currentNode)
        # remove node from unvisited nodes
        unvisitedNodes.remove(currentNode)

    return visitedNodes


def inNodelist(node, nodelist):
    for lnode in nodelist:
        if node.__eq__(lnode):
            return True, lnode
    return False, None


def updateNode(heightmap, visitedNodes, unvisitedNodes, currentNode, direction):
    if heightmap[currentNode.x][currentNode.y] == 'S':
        cv = ord('a')
    else:
        cv = ord(heightmap[currentNode.x][currentNode.y])  # currentnode value
    if direction == 'up':
        directionNode = node(currentNode.value + 1, currentNode.x - 1, currentNode.y, currentNode)
    elif direction == 'down':
        directionNode = node(currentNode.value + 1, currentNode.x + 1, currentNode.y, currentNode)
    elif direction == 'right':
        directionNode = node(currentNode.value + 1, currentNode.x, currentNode.y + 1, currentNode)
    else:  # --> left
        directionNode = node(currentNode.value + 1, currentNode.x, currentNode.y - 1, currentNode)

    # check if node was already visited
    if inNodelist(directionNode, visitedNodes)[0]:
        return unvisitedNodes

    # check if node needs to be added or updated # TODO FEHLER BEIM löschen von Nodes
    if heightmap[directionNode.x][directionNode.y] == 'S':
        dv = ord('a')
    else:
        dv = ord(heightmap[directionNode.x][directionNode.y])  # direction node value
    if (cv + 1 == dv) | (cv == dv) | (
            cv - 1 == dv):  # check if currentNode is on the same level or +- 1 as directionNode
        inList, lNode = inNodelist(directionNode, unvisitedNodes)
        if inList:
            if directionNode.value < lNode.value:  # update list node
                print('update')
                unvisitedNodes.remove(lNode)
                unvisitedNodes.append(directionNode)
        else:
            print('new')
            unvisitedNodes.append(directionNode)  # create new node

    print(f'updateNode len(unvisitedNodes) {len(unvisitedNodes)}')
    for i, un in enumerate(unvisitedNodes):
        print(f'{i}. updateNode {un}')

    return unvisitedNodes


if __name__ == '__main__':
    heightmap = loadData()

    start = findUniquePos(heightmap, 'S')
    end = findUniquePos(heightmap, 'E')

    nodemap = createNodeMap(heightmap, node(0, start[0], start[1], None), [], [])