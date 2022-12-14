def print_map(map):
    for l in map:
        print("".join(l))
    print("---")


def puzzle_func(fn, add_floor=False):
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines()]

        all_lines = []
        min_x = None  # left/right
        min_y = None  # up/down
        max_x = None
        max_y = None
        for row in lines:
            parts = row.split(" -> ")
            parts = [[int(x) for x in p.split(",")] for p in parts]

            for x, y in parts:
                if not min_x or min_x > x:
                    min_x = x
                if not max_x or max_x < x:
                    max_x = x

                if not min_y or min_y > y:
                    min_y = y
                if not max_y or max_y < y:
                    max_y = y

            all_lines.append(parts)

        map = [["." for __ in range(min_x, max_x + 1)] for _ in range(max_y + 1)]

        if add_floor:
            min_x -= 200
            for i, line in enumerate(map):
                map[i] = ["." for _ in range(200)] + line + ["." for _ in range(200)]

            map.append(["." for __ in range(min_x, max_x + 201)])
            map.append(["#" for __ in range(min_x, max_x + 201)])

        # draw the lines
        for line in all_lines:
            prev = None
            for x, y in line:
                if prev:
                    while prev != (x, y):
                        px, py = prev
                        map[py][px - min_x] = "#"

                        if px != x:
                            if px > x:
                                px -= 1
                            else:
                                px += 1
                        elif py != y:
                            if py > y:
                                py -= 1
                            else:
                                py += 1

                        map[py][px - min_x] = "#"
                        prev = (px, py)

                prev = (x, y)

        print_map(map)
        sand_source = (500 - min_x, 0)

        # sand falling
        i = 0

        try:
            while True:
                x, y = sand_source
                while True:
                    if map[y + 1][x] == ".":
                        y += 1
                    elif map[y + 1][x - 1] == ".":
                        y += 1
                        x -= 1
                    elif map[y + 1][x + 1] == ".":
                        y += 1
                        x += 1
                    else:
                        if map[y][x] == "o":
                            raise IndexError()
                        map[y][x] = "o"
                        break
                i += 1
        except IndexError:
            print_map(map)
            return i

    return 0


if __name__ == "__main__":
    result = puzzle_func("test.txt")
    assert result == 24

    result = puzzle_func("input.txt")
    print(result)
