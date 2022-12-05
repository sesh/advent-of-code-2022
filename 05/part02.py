from part01 import stacks_and_moves


def move_crates(fn):
    with open(fn) as f:
        lines = [l for l in f.readlines()]
        stacks, moves = stacks_and_moves(lines)

        for m in moves:
            count, source, dest = [int(x) for x in m.split() if x.isnumeric()]
            stacks[dest - 1] = stacks[source - 1][:count] + stacks[dest - 1]
            stacks[source - 1] = stacks[source - 1][count:]

        return "".join([s[0][1] for s in stacks])


if __name__ == "__main__":
    message = move_crates("test.txt")
    assert message == "MCD"

    message = move_crates("input.txt")
    print(message)
