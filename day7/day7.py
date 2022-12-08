# Structure of a node in the tree
    # Name     - Name of the Node
    # Type     - DIR; FILE
    # Value    - DIRECTORY --> List; File --> Size Value
    # Parent   - Object of the Parent
class Node:
    name = ''
    type = ''
    value = ''
    parent = None

    def __init__(self, name, type, value, parent):
        self.name = name
        self.type = type
        self.value = value
        self.parent = parent

def parseConsole(console, filesystem):
    currentPosConsole = 0
    while currentPosConsole < len(console):
        print(f'line {console[currentPosConsole]} consolePos {currentPosConsole}')

        if console[currentPosConsole] == '$ ls':
            res = ls(console,currentPosConsole,filesystem, currentNode)
            currentPosConsole = res[0]
            filesystem=res[1]
        elif console[currentPosConsole] == '$ cd /':
            currentNode = root
            currentPosConsole = currentPosConsole + 1
        elif console[currentPosConsole] == '$ cd ..':
            pass
            #cd_out()
        else:
            #res = cd_in(console[currentPosConsole][5:], currentPosConsole, currentPosFilesys)
            currentPosConsole = res[0]
            currentPosFilesys = res[1]
    return None

def ls(console,currentPosConsole,filesystem, currentNode):
    while currentPosConsole < len(console):
        line = console[currentPosConsole]
        if line.startswith('$'):
            return [currentPosConsole, filesystem]
        elif line.startswith('dir '):
            currentNode.value.append(Node(line[4:], 'DIR', [], currentNode))
            currentPosConsole = currentPosConsole + 1
        else:
            data = line.split(' ')
            currentNode.value.append(data[1], 'FILE', int(data[0]), currentNode)
            currentPosConsole = currentPosConsole + 1


def loadData():
    data = []
    with open('bspData.txt', 'r') as f:
        for line in f:
            data.append(line.replace('\n', ''))
    return data

if __name__ == '__main__':
    console = loadData()

    root = Node('/', 'DIR', [], None)
    currentNode = root

    parseConsole(console, root)

    # Part 2