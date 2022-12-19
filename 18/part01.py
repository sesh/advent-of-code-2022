import json
import numpy as np


def calculate_surface_area(space, max_dimension):
    surface_area = 0

    for x in range(max_dimension):
        for y in range(max_dimension):
            for z in range(max_dimension):
                if space[x, y, z] != "x":
                    continue

                if x > 0:
                    if space[x - 1, y, z] == ".":
                        surface_area += 1

                if x < max_dimension - 1:
                    if space[x + 1, y, z] == ".":
                        surface_area += 1

                if y > 0:
                    if space[x, y - 1, z] == ".":
                        surface_area += 1
                if y < max_dimension - 1:
                    if space[x, y + 1, z] == ".":
                        surface_area += 1
                if z > 0:
                    if space[x, y, z - 1] == ".":
                        surface_area += 1
                if z < max_dimension - 1:
                    if space[x, y, z + 1] == ".":
                        surface_area += 1

    return surface_area


def load_space(fn):
    with open(fn) as f:
        lines = [
            [int(x) for x in l.strip().split(",")] for l in f.readlines() if l.strip()
        ]

        max_dimension = 0
        for x, y, z in lines:
            if max([x, y, z]) > max_dimension:
                max_dimension = max([x, y, z])

        max_dimension += 3  # create a buffer around our array
        space = np.array(
            [
                [["." for x in range(max_dimension)] for t in range(max_dimension)]
                for m in range(max_dimension)
            ],
            str,
        )

        for x, y, z in lines:
            space[x + 1, y + 1, z + 1] = "x"

        return space, max_dimension


def puzzle_func(fn):
    space, max_dimension = load_space(fn)
    surface_area = calculate_surface_area(space, max_dimension)

    print(surface_area)
    return surface_area


if __name__ == "__main__":
    result = puzzle_func("test.txt")
    assert result == 64

    result = puzzle_func("input.txt")
    assert result == 3454
    print(result)
