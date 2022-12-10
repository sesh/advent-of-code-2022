def draw_pixel_if_appropriate(x, cycle, result):
    col = cycle

    while col > 39:
        col -= 40

    if x == col or x == col - 1 or x == col + 1:
        result[cycle-1] = "#"

    return result


def signal_strength(fn):
    result = ["." for _ in range(240)]

    with open(fn) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

        x = 1
        cycle = 0
        row = 0

        line = lines.pop(0)

        while line:
            cycle += 1
            result = draw_pixel_if_appropriate(x, cycle, result)

            if line.startswith("addx"):
                _, num = line.split()
                num = int(num)

                cycle += 1
                x += num
                result = draw_pixel_if_appropriate(x, cycle, result)

            line = None
            if lines:
                line = lines.pop(0)

    return result


if __name__ == "__main__":
    result = signal_strength("test.txt")
    for r in range(0, 250, 40):
        print("".join(result[r : r + 39]))

    print()

    result = signal_strength("input.txt")
    for r in range(0, 260, 40):
        print("".join(result[r : r + 39]))
