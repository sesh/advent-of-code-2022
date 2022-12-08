def visible_trees(fn):
    with open(fn) as f:
        lines = [[int(c) for c in l.strip()] for l in f.readlines() if l.strip()]
        tree_count = 0

        for x in range(len(lines[0])):
            for y in range(len(lines)):
                # bordering trees
                if x == 0 or y == 0 or x == len(lines[0]) - 1 or y == len(lines) - 1:
                    tree_count += 1
                else:
                    trees_left = [tree for tree in lines[x][:y]]
                    trees_right = [tree for tree in lines[x][(y + 1) :]]

                    vertical_trees = [lines[i][y] for i in range(len(lines[x]))]
                    trees_up = vertical_trees[:x]
                    trees_down = vertical_trees[(x + 1) :]

                    if all([tree < lines[x][y] for tree in trees_left]):
                        tree_count += 1
                    elif all([tree < lines[x][y] for tree in trees_right]):
                        tree_count += 1
                    elif all([tree < lines[x][y] for tree in trees_up]):
                        tree_count += 1
                    elif all([tree < lines[x][y] for tree in trees_down]):
                        tree_count += 1

    return tree_count


if __name__ == "__main__":
    result = visible_trees("test.txt")
    assert result == 21

    result = visible_trees("input.txt")
    print(result)
