class monkey:
    items = []
    operation = 'no operation'
    worryMultiplier = -1
    divisior = -1
    trueApe = None
    falseApe = None
    inspectedItemsCtr = 0

    def __init__(self, items, operation, worryMultiplier, divisior):
        self.items = items
        self.operation = operation
        self.worryMultiplier = worryMultiplier
        self.divisior = divisior

    def setPassApes(self, trueApe, falseApe):
        self.trueApe = trueApe
        self.falseApe = falseApe

    def option(self):
        for stresslevel in self.items:
            item = stresslevel
            if self.operation == '+':
                stresslevel += self.worryMultiplier
            elif self.operation == '*':
                if self.worryMultiplier == 'old':
                    stresslevel *= stresslevel
                else:
                    stresslevel *= self.worryMultiplier

            self.inspectedItemsCtr = self.inspectedItemsCtr + 1
            if (stresslevel % self.divisior) == 0:
                self.trueApe.items.append(item)
            else:
                self.falseApe.items.append(item)
        self.items = []

    def printMonkey(self, monkeyNr):
        if len(self.items) == 0:
            print(f'Monkey {monkeyNr}. Nah its empty')
        else:
            print(f'Monkey {monkeyNr}. items {self.items}, Inspected Items Ctr: {self.inspectedItemsCtr}')


if __name__ == '__main__':
    monkey0 = monkey([74, 64, 74, 63, 53], '*', 7, 5)
    monkey1 = monkey([69, 99, 95, 62], '*', 'old', 17)
    monkey2 = monkey([59, 81], '+', 8, 7)
    monkey3 = monkey([50, 67, 63, 57, 63, 83, 97], '+', 4, 13)
    monkey4 = monkey([61, 94, 85, 52, 81, 90, 94, 70], '+', 3, 19)
    monkey5 = monkey([69], '+', 5, 3)
    monkey6 = monkey([54, 55, 58], '+', 7, 11)
    monkey7 = monkey([79, 51, 83, 88, 93, 76], '*', 3, 2)

    monkey0.setPassApes(monkey1, monkey6)
    monkey1.setPassApes(monkey2, monkey5)
    monkey2.setPassApes(monkey4, monkey3)
    monkey3.setPassApes(monkey0, monkey7)
    monkey4.setPassApes(monkey6, monkey3)
    monkey5.setPassApes(monkey4, monkey2)
    monkey6.setPassApes(monkey1, monkey5)
    monkey7.setPassApes(monkey0, monkey6)

    monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

    ####### Testdata

    monkey0 = monkey([74, 64, 74, 63, 53], '*', 7, 5)
    monkey1 = monkey([69, 99, 95, 62], '*', 'old', 17)
    monkey2 = monkey([59, 81], '+', 8, 7)
    monkey3 = monkey([50, 67, 63, 57, 63, 83, 97], '+', 4, 13)
    monkey4 = monkey([61, 94, 85, 52, 81, 90, 94, 70], '+', 3, 19)
    monkey5 = monkey([69], '+', 5, 3)
    monkey6 = monkey([54, 55, 58], '+', 7, 11)
    monkey7 = monkey([79, 51, 83, 88, 93, 76], '*', 3, 2)

    monkey0.setPassApes(monkey1, monkey6)
    monkey1.setPassApes(monkey2, monkey5)
    monkey2.setPassApes(monkey4, monkey3)
    monkey3.setPassApes(monkey0, monkey7)
    monkey4.setPassApes(monkey6, monkey3)
    monkey5.setPassApes(monkey4, monkey2)
    monkey6.setPassApes(monkey1, monkey5)
    monkey7.setPassApes(monkey0, monkey6)

    monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

    #########################


    for i in range(0,20,1):
        print(f'Round {i+1}')
        for i, monkey in enumerate(monkeys):
            monkey.printMonkey(i)
            monkey.option()
            monkey.printMonkey(i)
        print()

    sum = 0
    for m in monkeys:
        sum = sum + m.inspectedItemsCtr

    print(f'Sum {sum}')