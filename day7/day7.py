# Structure of a node in the tree
# Name     - Name of the Node
# Type     - DIR; FILE
# Value    - DIRECTORY --> List; FILE --> Size Value
# Parent   - Object of the Parent
class Node:
    name = ''
    typ = ''
    size = 0
    value = ''
    parent = None

    def __init__(self, name, typ, size, value, parent):
        self.name = name
        self.typ = typ
        self.size = size
        self.value = value
        self.parent = parent


def printNode(node):
    if node.typ == 'DIR':
        print(f'- \'{node.name}\' (Type \'{node.typ}\', Size = {node.size})')
        for subitem in node.value:
            i = countParentNodes(subitem, 0)
            while i > 0:
                print("  ", end='')
                i = i - 1
            printNode(subitem)
    else:
        print(f'- \'{node.name}\' (Type \'{node.typ}\', Size = {node.size})')


def countParentNodes(node, parentCtr):
    if node.parent == None:
        return parentCtr
    else:
        parentCtr = parentCtr + 1
        return countParentNodes(node.parent, parentCtr)


def parseConsole(console, root, currentNode):
    currentPosConsole = 0
    while currentPosConsole < len(console):
        if console[currentPosConsole] == '$ ls':
            res = ls(console, currentPosConsole, currentNode)
            currentPosConsole = res[0]
            currentNode = res[1]
        elif console[currentPosConsole] == '$ cd /':
            currentNode = root
            currentPosConsole = currentPosConsole + 1
        elif console[currentPosConsole] == '$ cd ..':
            currentPosConsole = currentPosConsole + 1
            if currentNode.parent == None:
                continue
            currentNode = currentNode.parent
        else:
            currentNode = cd_in(console[currentPosConsole][5:], currentNode)
            currentPosConsole = currentPosConsole + 1
    return root


def ls(console, currentPosConsole, currentNode):
    currentPosConsole = currentPosConsole + 1
    while currentPosConsole < len(console):
        line = console[currentPosConsole]
        if console[currentPosConsole].startswith('$'):
            return [currentPosConsole, currentNode]
        elif line.startswith('dir '):
            currentNode.value.append(Node(line[4:], 'DIR', 0, [], currentNode))
            currentPosConsole = currentPosConsole + 1
        else:
            data = line.split(' ')
            currentNode.value.append(Node(data[1], 'FILE', int(data[0]), None, currentNode))
            currentPosConsole = currentPosConsole + 1
    return [currentPosConsole, currentNode]


def cd_in(name, currentNode):
    for dir in currentNode.value:
        if dir.name == name:
            return dir


def loadData():
    data = []
    with open('Data.txt', 'r') as f:
        for line in f:
            data.append(line.replace('\n', ''))
    return data


def p1(node):
    global totalSum
    if node.typ == 'DIR':
        for subitem in node.value:
            if subitem.typ == 'DIR':
                if subitem.size < 100000:
                    # print(f'Node under 100k {subitem.name} {subitem.size}')
                    totalSum = totalSum + subitem.size
                p1(subitem)


def p2(node):
    global delSize
    global delDirSize

    if node.typ == 'DIR':
        for subitem in node.value:
            if (subitem.typ == 'DIR') & (subitem.size > delSize) & (subitem.size < delDirSize):
                #print(f'subitem.size {subitem.size} > delSize {delSize} --> {subitem.size > delSize}')
                delDirSize = subitem.size
            p2(subitem)

def sumDir(filesystem):
    for node in filesystem.value:
        if node.typ == 'DIR':
            sumDir(node)
        filesystem.size = filesystem.size + node.size


if __name__ == '__main__':
    console = loadData()

    filesystem = Node('/', 'DIR', 0, [], None)
    filesystem = parseConsole(console, filesystem, filesystem)
    sumDir(filesystem)
    #printNode(filesystem)

    # Part 1
    totalSum = 0
    p1(filesystem)
    print(totalSum)

    # Part 2
    # Size of Total Space       70000000
    # Size of Update            30000000
    freeSpace = 70000000 - filesystem.size
    delSize = 30000000 - freeSpace
    delDirSize = 70000000
    p2(filesystem)
    print(delDirSize)
