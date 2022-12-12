from part01 import create_graph, bfs


def moves_to_target(fn):
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines()]
        graph, _, end, low_points = create_graph(lines)

        results = []
        for start in low_points:
            result = bfs(graph, start, end)
            if result:
                results.append(len(result) - 1)

        return min(results)


if __name__ == "__main__":
    result = moves_to_target("test.txt")
    assert result == 29

    result = moves_to_target("input.txt")
    print(result)
