def get_most_scenic_score(fn):
    with open(fn) as f:
        lines = [[int(c) for c in l.strip()] for l in f.readlines() if l.strip()]
        most_scenic = 0

        for x in range(len(lines[0])):
            for y in range(len(lines)):
                vertical_trees = [lines[i][y] for i in range(len(lines[x]))]

                trees_left = [tree for tree in lines[x][:y]]
                trees_right = [tree for tree in lines[x][(y + 1) :]]
                trees_up = vertical_trees[:x]
                trees_down = vertical_trees[(x + 1) :]

                trees_left.reverse()
                trees_up.reverse()

                tree = lines[x][y]
                up, right, down, left = 0, 0, 0, 0

                for t in trees_up:
                    up += 1
                    if t >= tree:
                        break

                for t in trees_right:
                    right += 1
                    if t >= tree:
                        break

                for t in trees_down:
                    down += 1
                    if t >= tree:
                        break

                for t in trees_left:
                    left += 1
                    if t >= tree:
                        break

                score = up * right * down * left
                if score > most_scenic:
                    most_scenic = score

    return most_scenic


if __name__ == "__main__":
    result = get_most_scenic_score("test.txt")
    assert result == 8

    result = get_most_scenic_score("input.txt")
    print(result)
