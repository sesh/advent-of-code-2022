from part01 import compare
import json


class Packet:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return compare(self.val, other.val)


def order_pairs(fn):
    with open(fn) as f:
        lines = [Packet(json.loads(l)) for l in f.readlines() if l.strip()]
        lines.append(Packet([[2]]))
        lines.append(Packet([[6]]))

        lines = sorted(lines)
        lines = [l.val for l in lines]

        return (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)


if __name__ == "__main__":
    result = order_pairs("test.txt")
    assert result == 140

    result = order_pairs("input.txt")
    print(result)
