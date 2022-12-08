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

console = []
currentPosConsole = 0


def loadData():
    with open('bspData.txt', 'r') as f:
        for line in f:
            console.append(line.replace('\n', ''))
    return console


def parseConsole():
    while currentPosConsole < len(console):
        print(console[currentPosConsole])

        if console[currentPosConsole] == '$ ls':
            ls()
        elif console[currentPosConsole] == '$ cd /':
            cd_root()
        elif console[currentPosConsole] == '$ cd ..':
            cd_out()
        else:
            cd_in(console[currentPosConsole][5:])


def cd_in(name):
    #nonlocal currentPosConsole
    #nonlocal currentPosFilesys
    currentPosConsole = currentPosConsole + 1

    if currentPosFilesys['NAME'] == name:
        print(f'Name: {name} Already in directory {currentPosFilesys}')
        return

    for dir in currentPosFilesys['VALUE']:
        if dir['TYPE'] == 'FILE':
            continue
        else:
            if dir['NAME'] == name:
                currentPosFilesys = dir
                break

def cd_out():
    pass


def cd_root():
    pass


def ls():
    pass


def addNode():
    pass


if __name__ == '__main__':
    # Part 1
    loadData()

    print(filesys)

    # Part 2
