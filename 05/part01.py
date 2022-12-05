import textwrap


def stacks_and_moves(lines):
    crates = []
    moves = []
    doing_crates = True
    for l in lines:
        if l.strip() == "":
            doing_crates = False
        elif doing_crates:
            crates.append(l.rstrip())
        else:
            moves.append(l)

    num_stacks = int(crates[-1].split()[-1])
    stacks = [[] for _ in range(num_stacks)]

    for row in crates[:-1]:
        crates = textwrap.wrap(row, 4, drop_whitespace=False)
        for i, crate in enumerate(crates):
            if crate.strip():
                stacks[i].append(crate.strip())

    return stacks, moves


def move_crates(fn):
    with open(fn) as f:
        lines = [l for l in f.readlines()]

        stacks, moves = stacks_and_moves(lines)

        for m in moves:
            count, source, dest = [int(x) for x in m.split() if x.isnumeric()]

            for i in range(count):
                stacks[dest - 1].insert(0, stacks[source - 1].pop(0))

        return "".join([s[0][1] for s in stacks])


if __name__ == "__main__":
    message = move_crates("test.txt")
    assert message == "CMZ"

    message = move_crates("input.txt")
    print(message)
