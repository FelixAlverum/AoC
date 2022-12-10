# Read calorie data per elf file
def readData():
    elflist = []
    with open('data.txt', 'r') as f:
        elf_ctr = 0
        for i, line in enumerate(f):
            line = line.replace('\n', '')
            if line == '':
                elf_ctr = elf_ctr + 1
                continue
            elflist.append([elf_ctr, int(line)])
    return elflist

def sumCalories(elflist):
    sumElf = [0, 0]
    sumElfList = []
    for elf in elflist:
        #prüfe ob ein neuer da ist
        if sumElf[0] != elf[0]:
            sumElfList.append(sumElf)
            sumElf = [sumElf[0]+1, 0]
        sumElf[1] = sumElf[1] + elf[1]
    return sumElfList

def findMaxElf(elflist):
    maxElf = [0,0]
    for elf in elflist:
        if maxElf[1] < elf[1]:
            maxElf = elf
    return maxElf

def findTopThree(elflist):
    maxelf1 = findMaxElf(elflist)
    elflist.remove(maxelf1)
    maxelf2 = findMaxElf(elflist)
    elflist.remove(maxelf2)
    maxelf3 = findMaxElf(elflist)

    sumCal = maxelf1[1] + maxelf2[1] + maxelf3 [1]
    print(f'sum top 3 cal: {sumCal}')

    return [maxelf1, maxelf2, maxelf3]

if __name__ == '__main__':
    elflist = sumCalories(readData())
    maxelf = findMaxElf(elflist)
    print(f'Max Elf has the nr {maxelf[0]} and carries {maxelf[1]} calories')
    elflist = findTopThree(elflist)
    for i, elf in enumerate(elflist):
         print(f'elf {elf[0]} has {elf[1]} cal')