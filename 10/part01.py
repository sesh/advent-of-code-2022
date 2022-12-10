KEY_CYCLES = [x for x in range(20, 1000, 40)]


def signal_strength(fn):
    result = 0
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

        x = 1
        cycle = 0

        line = lines.pop(0)

        while line:
            cycle += 1
            if cycle in KEY_CYCLES:
                result += cycle * x

            if line.startswith("addx"):
                _, num = line.split()
                num = int(num)

                cycle += 1
                if cycle in KEY_CYCLES:
                    result += cycle * x

                x += num

            line = None
            if lines:
                line = lines.pop(0)

    return result


if __name__ == "__main__":
    result = signal_strength("test.txt")
    print(result)
    assert result == 13140

    result = signal_strength("input.txt")
    print(result)
