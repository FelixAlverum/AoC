import math


# inspect --> relive --> pass to monkey


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
            self.inspectedItemsCtr += 1

            # inspect item
            if self.operation == '+':
                stresslevel += self.worryMultiplier
            elif self.operation == '*':
                if self.worryMultiplier == 'old':
                    stresslevel *= stresslevel
                else:
                    stresslevel *= self.worryMultiplier

            # relive
            stresslevel = stresslevel // 3

            # pass item
            if stresslevel % self.divisior == 0:
                self.trueApe.items.append(stresslevel)
            else:
                self.falseApe.items.append(stresslevel)
        self.items = []

    def option2(self):
        #divisors 2; 3; 5; 7; 11, 13, 17, 19
        for stresslevel in self.items:
            self.inspectedItemsCtr += 1

            # inspect item
            if self.operation == '+':
                stresslevel += self.worryMultiplier
            elif self.operation == '*':
                if self.worryMultiplier == 'old':
                    stresslevel *= stresslevel
                else:
                    stresslevel *= self.worryMultiplier

            if not stresslevel % (2*3*5*7*11*13*17*19) == 0:
                stresslevel = stresslevel % (2*3*5*7*11*13*17*19)

            #For Test
            #if not stresslevel % (23*19*13*17) == 0:
            #    stresslevel = stresslevel % (23*19*13*17)

            # pass item
            if stresslevel % self.divisior == 0:
                self.trueApe.items.append(stresslevel)
            else:
                self.falseApe.items.append(stresslevel)
        self.items = []

    def printMonkey(self, monkeyNr):
        if len(self.items) == 0:
            print(f'Monkey {monkeyNr}. Nah its empty, Inspected Items Ctr: {self.inspectedItemsCtr}')
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
    monkey4.setPassApes(monkey7, monkey3)
    monkey5.setPassApes(monkey4, monkey2)
    monkey6.setPassApes(monkey1, monkey5)
    monkey7.setPassApes(monkey0, monkey6)

    monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

    """# Testdata

    monkey0 = monkey([79, 98], '*', 19, 23)
    monkey1 = monkey([54, 65, 75, 74], '+', 6, 19)
    monkey2 = monkey([79, 60, 97], '*', 'old', 13)
    monkey3 = monkey([74], '+', 3, 17)

    monkey0.setPassApes(monkey2, monkey3)
    monkey1.setPassApes(monkey2, monkey0)
    monkey2.setPassApes(monkey1, monkey3)
    monkey3.setPassApes(monkey0, monkey1)

    monkeys = [monkey0, monkey1, monkey2, monkey3]

    #########################

    #Part 1
    for i in range(0,20,1):
        print(f'Round {i+1}')
        for i, monkey in enumerate(monkeys):
            monkey.printMonkey(i)
            monkey.option()
            monkey.printMonkey(i)
        print()

    monkeyBusiness = []
    for m in monkeys:
        monkeyBusiness.append(m.inspectedItemsCtr)
    monkeyBusiness.sort(reverse=True)
    print(f'monkeybusiness {monkeyBusiness} --> {monkeyBusiness[0]} * {monkeyBusiness[1]} = {monkeyBusiness[0] *monkeyBusiness[1]}')
    """
    # Part 2
    for i in range(1, 10001, 1):
        for monkey in monkeys:
            monkey.option2()
        if (i == 1) | (i == 20) | (i%1000 == 0):
            print(f'== After Round {i} ==')
            for index, m in enumerate(monkeys):
                print(f' monkey {index} has inspected items {m.inspectedItemsCtr} times')
            print()

    monkeyBusiness = []
    for m in monkeys:
        monkeyBusiness.append(m.inspectedItemsCtr)
    monkeyBusiness.sort(reverse=True)
    print(f'monkeybusiness {monkeyBusiness} --> {monkeyBusiness[0]} * {monkeyBusiness[1]} = {monkeyBusiness[0] * monkeyBusiness[1]}')