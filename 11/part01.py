from math import floor
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
        self.op, self.num = self.operation.split()[-2:]
        self.div_x = int(self.test.split()[-1])

        self.use_old = self.num == "old"

        if not self.use_old:
            self.num = int(self.num)

    def test_item(self, item, round=""):
        result = item % self.div_x == 0
        return result

    def inspect_item(self, item):
        self.inspections += 1

        if self.use_old:
            num = item
        else:
            num = self.num

        if self.op == "+":
            result = num + item
            return result
        elif self.op == "*":
            result = num * item
            return result


def puzzle_func(fn, rounds, use_relief=True):
    with open(fn) as f:
        input = f.read()
        monkeys = []

        for m in input.split("Monkey ")[1:]:
            lines = [m[0].replace(":", "").strip()] + [
                l.split(":")[-1].strip() for l in m.splitlines()[1:] if l.strip()
            ]
            monkeys.append(Monkey(*lines))

        lcm = 1
        for m in monkeys:
            lcm = lcm * m.div_x

        for round in range(rounds):
            for monkey in monkeys:
                while monkey.items:
                    initial = monkey.items.pop(0)
                    new = monkey.inspect_item(initial)

                    if use_relief:
                        i = floor(new / 3)
                    else:
                        i = new % lcm

                    if monkey.test_item(i, round=round):
                        monkeys[monkey.if_true_dest].items.append(i)
                    else:
                        monkeys[monkey.if_false_dest].items.append(i)

    sorted_inspections = sorted([m.inspections for m in monkeys], reverse=True)[:2]
    print(sorted_inspections)
    return sorted_inspections[0] * sorted_inspections[1]


if __name__ == "__main__":
    result = puzzle_func("test.txt", 20)
    assert result == 10605

    result = puzzle_func("input.txt", 20)
    print(result)
