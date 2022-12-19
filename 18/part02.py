import json
import numpy as np

from part01 import calculate_surface_area, load_space


def can_reach_edge(array, x, y, z, visited=None):
    if visited is None:
        visited = np.zeros(array.shape)

    # print(array, x, y, z, visited)

    # Check if the current point is out of bounds or has the value "x"
    if (
        x < 0
        or x >= array.shape[0]
        or y < 0
        or y >= array.shape[1]
        or z < 0
        or z >= array.shape[2]
        or array[x, y, z] == "x"
        or visited[x, y, z] == 1
    ):
        return False

    # Check if the current point is at the edge of the array
    if (
        x == 0
        or x == array.shape[0] - 1
        or y == 0
        or y == array.shape[1] - 1
        or z == 0
        or z == array.shape[2] - 1
    ):
        return True

    # Mark the current point as visited
    visited[x, y, z] = 1

    # Recursively check the surrounding points
    if (
        can_reach_edge(array, x - 1, y, z, visited)
        or can_reach_edge(array, x + 1, y, z, visited)
        or can_reach_edge(array, x, y - 1, z, visited)
        or can_reach_edge(array, x, y + 1, z, visited)
        or can_reach_edge(array, x, y, z - 1, visited)
        or can_reach_edge(array, x, y, z + 1, visited)
    ):
        return True

    return False


def fill_space(space, max_dimension):
    for x in range(max_dimension):
        for y in range(max_dimension):
            for z in range(max_dimension):
                # If the current space is a ".", check if you can reach the edge
                if space[x, y, z] == ".":
                    if not can_reach_edge(space, x, y, z):
                        space[x, y, z] = "x"

    return space


def puzzle_func(fn):
    space, max_dimension = load_space(fn)
    space = fill_space(space, max_dimension)
    print(space[3, 3, 6])
    surface_area = calculate_surface_area(space, max_dimension)

    return surface_area


if __name__ == "__main__":
    result = puzzle_func("test.txt")
    print(result)
    assert result == 58

    result = puzzle_func("input.txt")
    assert result < 3250
    print(result)
