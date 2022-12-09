from part01 import get_valid_tail_position, is_valid_tail_position, move_head


def navigate_grid(fn):
    with open(fn) as f:
        moves = [l.strip().split() for l in f.readlines()]

        #      (up, right)
        head = (0, 0)
        tail = [(0, 0) for _ in range(9)]

        tail_positions = [(tail[8][0], tail[8][1])]

        for direction, count in moves:
            for _ in range(int(count)):
                head = move_head(head, direction)

                # move tail to valid position
                for i, t in enumerate(tail):
                    prev = tail[i - 1] if i > 0 else head
                    tail[i] = get_valid_tail_position(prev, t)

                    if i == 8:
                        tail_positions.append((tail[-1][0], tail[-1][1]))

    return len(set(tail_positions))


if __name__ == "__main__":
    result = navigate_grid("test_larger.txt")
    print(result)
    assert result == 36

    result = navigate_grid("input.txt")
    print(result)
    assert result == 2458
