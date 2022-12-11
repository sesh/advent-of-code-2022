from math import floor
from gmpy2 import mpz

import time

class Monkey:

    def __init__(self, num, items, operation, test, if_true, if_false):
        self.num = num
        self.items = [int(x) for x in items.split(",")]
        self.operation = operation
        self.test = test
        self.if_true_dest = int(if_true.split()[-1])
        self.if_false_dest = int(if_false.split()[-1])
        self.inspections = 0

    def test_item(self, item, round=""):
        if self.test.startswith("divisible by"):
            x = int(self.test.split()[-1])
            t = time.time()
            print("doing mod")
            result = item % x == 0
            print(f"done mod {time.time() - t} {round}")
            return result
        else:
            print("Did not parse test")

    def inspect_item(self, item):
        print('a')
        self.inspections += 1
        op, num = self.operation.split()[-2:]
        print('b')
        if num == 'old':
            num = item

        if op == '+':
            print('c')
            result = int(num) + item
            print('d')
            return result
        elif op == '*':
            print('e')
            result = int(num) * mpz(item)
            print('f')
            return result
        else:
            print("Unexpected operation")



def puzzle_func(fn, rounds, use_relief=True):
    with open(fn) as f:
        input = f.read()
        monkeys = []

        for m in input.split("Monkey ")[1:]:
            lines = [m[0].replace(':', '').strip()] + [l.split(':')[-1].strip() for l in m.splitlines()[1:] if l.strip()]
            monkeys.append(Monkey(*lines))

        for round in range(rounds):
            print(round)
            for monkey in monkeys:
                while monkey.items:
                    print('1')
                    initial = monkey.items.pop(0)

                    new = monkey.inspect_item(initial)
                    print('2')

                    # relief?!
                    if use_relief:
                        i = floor(new/3)
                    else:
                        i = new

                    if monkey.test_item(i, round=round):
                        monkeys[monkey.if_true_dest].items.append(i)
                    else:
                        monkeys[monkey.if_false_dest].items.append(i)
                    print('3')

    sorted_inspections = sorted([m.inspections for m in monkeys], reverse=True)[:2]
    print(sorted_inspections)
    return sorted_inspections[0] * sorted_inspections[1]


if __name__ == "__main__":
    result = puzzle_func("test.txt", 20)
    assert result == 10605

    result = puzzle_func("input.txt", 20)
    print(result)
