def loadData():
    data = []
    with open('Data.txt', 'r') as f:
        i = 0
        for line in f:
            data.append([])
            line = line.replace('\n', '')
            for c in line:
                data[i].append(int(c))
            i = i + 1
    return data

def countVisibleTrees(grid):
    visibleTrees = 0

    for row in range(0, len(grid), 1):
        for col in range(0, len(grid[row]), 1):

            # edge case
            if (row == 0) | (row == len(grid)-1) | (col == 0) | (col == len(grid[row])-1):
                visibleTrees = visibleTrees + 1
                continue

            tree = grid[row][col]
            treeBigger = False

            # look from top
            treesBetweenEdge = reversed(range(0, row, 1))
            for compareRow in treesBetweenEdge:
                if (tree < grid[compareRow][col]) | (tree == grid[compareRow][col]):
                    break
                elif compareRow == 0:
                    visibleTrees = visibleTrees + 1
                    treeBigger = True

            if treeBigger:
                continue

            # look from bottom
            treesBetweenEdge = reversed(range(row+1, len(grid), 1))
            for compareRow in treesBetweenEdge:
                if (tree < grid[compareRow][col]) | (tree == grid[compareRow][col]):
                    break
                elif compareRow == row+1:
                    visibleTrees = visibleTrees + 1
                    treeBigger = True

            if treeBigger:
                continue

            treesBetweenEdge = reversed(range(0, col, 1))
            # look from left
            for compareCol in treesBetweenEdge:
                if (grid[row][col] < grid[row][compareCol]) | (grid[row][col] == grid[row][compareCol]):
                    break
                elif compareCol == 0:
                    visibleTrees = visibleTrees + 1
                    treeBigger = True
            if treeBigger:
                continue

            # look from right
            treesBetweenEdge = reversed(range(col+1, len(grid[row]), 1))
            for compareCol in treesBetweenEdge:
                if (grid[row][col] < grid[row][compareCol]) | (grid[row][col] == grid[row][compareCol]):
                    break
                elif compareCol == col+1:
                    visibleTrees = visibleTrees + 1
                    treeBigger = True
            if treeBigger:
                continue

    print(visibleTrees)

def calculateScenicScore(grid):
    maxScenicView = -1;
    for row in range(0, len(grid), 1):
        for col in range(0, len(grid[row]), 1):
            scenicView = 1

            tree = grid[row][col]
            distance = 0

            #print(f'tree {tree} row {row} col {col}')
            # look from top
            treesBetweenEdge = reversed(range(0, row, 1))
            for compareRow in treesBetweenEdge:
                distance = distance + 1
                if (tree < grid[compareRow][col]) | (tree == grid[compareRow][col] | (compareRow == 0)):
                    break
            #print(f'(up) {distance}', end=' * ')
            scenicView = scenicView * distance
            distance = 0

            # look from bottom
            treesBetweenEdge = range(row+1, len(grid), 1)
            for compareRow in treesBetweenEdge:
                distance = distance + 1
                if (tree < grid[compareRow][col]) | (tree == grid[compareRow][col] | (compareRow == len(grid)-1)):
                    break
            #print(f'(down) {distance}', end=' * ')
            scenicView = scenicView * distance
            distance = 0

            treesBetweenEdge = reversed(range(0, col, 1))
            # look from left
            for compareCol in treesBetweenEdge:
                distance = distance + 1
                if (grid[row][col] < grid[row][compareCol]) | (grid[row][col] == grid[row][compareCol] | (compareCol == 0)):
                    break
            #print(f'(left) {distance}', end=' * ')
            scenicView = scenicView * distance
            distance = 0

            # look from right
            treesBetweenEdge = range(col+1, len(grid[row]), 1)
            for compareCol in treesBetweenEdge:
                distance = distance + 1
                if (grid[row][col] < grid[row][compareCol]) | (grid[row][col] == grid[row][compareCol] | (compareCol == len(grid[row])-1)):
                    break
            #print(f'(right) {distance}', end=' = ')
            scenicView = scenicView * distance
            #print(scenicView)

            if scenicView > maxScenicView:
                maxScenicView = scenicView

    print(maxScenicView)

if __name__ == '__main__':
    grid = loadData()
    #for i in grid:
    #    for j in i:
    #        print(f'{j}', end=' ')
    #    print('')

    # Part 1
    countVisibleTrees(grid)

    # Part 2
    calculateScenicScore(grid)