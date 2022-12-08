def loadData():
    data = []
    with open('bspData.txt', 'r') as f:
        for line in f:
            data.append(line.replace('\n', ''))
    return data


def parseConsole(filesys, currentPosFilesys, console, currentPosConsole):
    while currentPosConsole < len(console):
        print(f'line{console[currentPosConsole]} consolePos {currentPosConsole}')

        if console[currentPosConsole] == '$ ls':
            ls()
        elif console[currentPosConsole] == '$ cd /':
            res = cd_root(filesys, currentPosFilesys, currentPosConsole)
            filesys = res[0]
            currentPosFilesys = res[1]
            currentPosConsole = res[2]
        elif console[currentPosConsole] == '$ cd ..':
            cd_out()
        else:
            res = cd_in(console[currentPosConsole][5:], currentPosConsole, currentPosFilesys)
            currentPosConsole = res[0]
            currentPosFilesys = res[1]
    return [filesys, currentPosFilesys, console, currentPosConsole]


def cd_in(name, currentPosConsole, currentPosFilesys):
    currentPosConsole = currentPosConsole + 1

    if currentPosFilesys['NAME'] == name:
        print(f'Name: {name} Already in directory {currentPosFilesys}')
        return [currentPosConsole, currentPosFilesys]

    for dir in currentPosFilesys['VALUE']:
        if dir['TYPE'] == 'FILE':
            continue
        else:
            if dir['NAME'] == name:
                currentPosFilesys = dir
                break
    print(f'currentPosConsole {currentPosConsole} currentPosFilesys {currentPosFilesys}')
    return [currentPosConsole, currentPosFilesys]

def cd_out():
    pass


def cd_root(filesys, currentPosFilesys, currentPosConsole):
    currentPosConsole = currentPosConsole + 1
    currentPosFilesys = filesys
    return filesys, currentPosFilesys, currentPosConsole



def ls():
    pass


def addNode():
    pass


if __name__ == '__main__':
    # Structure of a node in the tree
    # Name     - Name of the Node
    # Type     - DIR; FILE
    # Value    - DIRECTORY --> List; File --> Size Value
    # Parent   - Object of the Parent
    filesys = {'NAME': '/',
               'TYPE': 'DIR',
               'VALUE': [],
               'PARENT': None
               }
    currentPosFilesys = filesys

    console = loadData()
    currentPosConsole = 0

    # Part 1
    response = parseConsole(filesys, currentPosFilesys, console, currentPosConsole)

    filesys = response[0]
    currentPosFilesys = response[1]
    console= response[2]
    currentPosConsole = response[3]

    #print(filesys)

    # Part 2
