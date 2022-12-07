def readData():
    games = []
    with open('data.txt', 'r') as f:
        for i, line in enumerate(f):
            games.append(line.replace('\n',''))
    return games

def calculatePoints1(games):
    points = 0
    for game in games:
        #print(game)
        if game == 'A X':
            points = points + 1 + 3
        if game == 'A Y':
            points = points + 2 + 6
        if game == 'A Z':
            points = points + 3 + 0
        if game == 'B X':
            points = points + 1 + 0
        if game == 'B Y':
            points = points + 2 + 3
        if game == 'B Z':
            points = points + 3 + 6
        if game == 'C X':
            points = points + 1 + 6
        if game == 'C Y':
            points = points + 2 + 0
        if game == 'C Z':
            points = points + 3 + 3
    print(f'Points Round 1: {points}')
    return points

def calculatePoints2(games):
    points = 0
    # X --> Lose        A = Rock     = 1
    # Y --> Draw        B = Paper    = 2
    # Z --> Win         C = Scissors = 3
    for game in games:
        if game == 'A X':
            points = points + 3 + 0
        if game == 'A Y':
            points = points + 1 + 3
        if game == 'A Z':
            points = points + 2 + 6
        if game == 'B X':
            points = points + 1 + 0
        if game == 'B Y':
            points = points + 2 + 3
        if game == 'B Z':
            points = points + 3 + 6
        if game == 'C X':
            points = points + 2 + 0
        if game == 'C Y':
            points = points + 3 + 3
        if game == 'C Z':
            points = points + 1 + 6
    print(f'Points Round 2: {points}')
    return points

if __name__ == '__main__':
    calculatePoints1(readData())
    calculatePoints2(readData())
