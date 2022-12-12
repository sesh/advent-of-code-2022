import string
import random
from collections import deque


LETTERS = string.ascii_lowercase


def get_value(s):
    if s in LETTERS:
        return LETTERS.index(s)
    elif s == "S":
        return LETTERS.index("a")
    elif s == "E":
        return LETTERS.index("z")


def bfs(graph, start, end):
    q = []
    parents = {}

    explored = [start]
    q.append(start)

    while q != []:
        v = q.pop(0)
        if v == end:
            # found the end
            result = [v]
            while True:
                n = parents.get(v)
                if not n:
                    return result
                result.append(n)
                v = n

        for w in graph[v]:
            if w not in explored:
                parents[w] = v
                explored.append(w)
                q.append(w)


def create_graph(lines):

    # set up
    graph = {}
    start = None
    end = None
    low_points = []

    for row, line in enumerate(lines):
        for col, value in enumerate(line):
            if value == "S":
                start = str((row, col))
                value = "a"

            if value == "E":
                end = str((row, col))
                value = "z"

            if value == "a":
                low_points.append(str((row, col)))

            max_val = get_value(value) + 1
            valid_moves = [
                x
                for x in [
                    (row - 1, col)
                    if row != 0 and get_value(lines[row - 1][col]) <= max_val
                    else None,
                    (row + 1, col)
                    if row < len(lines) - 1
                    and get_value(lines[row + 1][col]) <= max_val
                    else None,
                    (row, col - 1)
                    if col != 0 and get_value(lines[row][col - 1]) <= max_val
                    else None,
                    (row, col + 1)
                    if col < len(lines[0]) - 1
                    and get_value(lines[row][col + 1]) <= max_val
                    else None,
                ]
                if x
            ]

            graph[str((row, col))] = [str(x) for x in valid_moves]

    return graph, start, end, low_points


def moves_to_target(fn):
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines()]
        graph, start, end, _ = create_graph(lines)
        result = bfs(graph, start, end)
        return len(result) - 1


if __name__ == "__main__":
    result = moves_to_target("test.txt")
    assert result == 31

    result = moves_to_target("input.txt")
    print(result)
