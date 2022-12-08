# Structure of a node in the tree
    # Name     - Name of the Node
    # Type     - DIR; FILE
    # Size     - File --> Size Value
    # Value    - DIRECTORY --> List;
    # Parent   - Object of the Parent
class Node:
    name = ''
    typ = ''
    value = ''
    parent = None

    def __init__(self, name, typ, value, parent):
        self.name = name
        self.typ = typ
        self.value = value
        self.parent = parent

def parseConsole(console, root, currentNode):
    currentPosConsole = 0
    while currentPosConsole < len(console):
        print(f'line {console[currentPosConsole]} consolePos {currentPosConsole}')

        if console[currentPosConsole] == '$ ls':
            res = ls(console,currentPosConsole, currentNode)
            currentPosConsole = res[0]
            currentNode=res[1]
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
    return None

def ls(console,currentPosConsole, currentNode):
    currentPosConsole = currentPosConsole + 1
    while currentPosConsole < len(console):
        line = console[currentPosConsole]
        print(line)
        if console[currentPosConsole].startswith('$'):
            return [currentPosConsole, currentNode]
        elif line.startswith('dir '):
            currentNode.value.append(Node(line[4:], 'DIR', [], currentNode))
            currentPosConsole = currentPosConsole + 1
        else:
            data = line.split(' ')
            currentNode.value.append(Node(data[1], 'FILE', int(data[0]), currentNode))
            currentPosConsole = currentPosConsole + 1

def cd_in(name, currentNode):
    for dir in currentNode.value:
        if dir.name == name:
            return dir


def loadData():
    data = []
    with open('bspData.txt', 'r') as f:
        for line in f:
            data.append(line.replace('\n', ''))
    return data

if __name__ == '__main__':
    console = loadData()

    filesystem = Node('/', 'DIR', [], None)
    parseConsole(console, filesystem, filesystem)

    # Part 2