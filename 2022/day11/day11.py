class monkey:
    items = []
    operation = 'no operation'
    worryMultiplier = -1
    divisior = -1
    def __init__(self, items, operation, worryMultiplier, divisior):
        self.items = items
        self.operation = operation
        self.worryMultiplier = worryMultiplier
        self.divisior = divisior

    def operation(self, trueApe, falseApe):
        for stresslevel in self.items:
            item = stresslevel
            if self.operation == '+':
                stresslevel += self.worryMultiplier
            elif self.operation == '*':
                stresslevel *= self.worryMultiplier
            elif self.operation == 'old':
                stresslevel *= stresslevel

            if stresslevel % self.division == 0:
                trueApe.items.append(item)
            else:
                falseApe.items.appemd(item)
        self.items = []
        return [trueApe, falseApe]

def opMonkey1 (parameter):
    print(f'testfunction {parameter}')


if __name__ == '__main__':
    monkey0 = monkey([74, 64, 74, 63, 53], '*', 7, 5)
    monkey1 = monkey([69, 99, 95, 62], '*', 'old', 17)
    monkey2 = monkey([59, 81], '+', 8, 7)
    monkey3 = monkey([50, 67, 63, 57, 63, 83, 97], '+', 4, 13)
    monkey4 = monkey([69], '+', 5, 19)
    monkey5 = monkey([74, 64, 74, 63, 53], '*', 7, 5)
    monkey6 = monkey([74, 64, 74, 63, 53], '*', 7, 5)
    monkey7 = monkey([74, 64, 74, 63, 53], '*', 7, 5)