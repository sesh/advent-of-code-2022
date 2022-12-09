def is_valid_tail_position(head, tail):
    # must be adjacent
    if head[0] == tail[0]:
        # same row
        if head[1] == tail[1] or head[1] == tail[1] - 1 or head[1] == tail[1] + 1:
            return True

    if head[1] == tail[1]:
        if head[0] == tail[0] or head[0] == tail[0] - 1 or head[0] == tail[0] + 1:
            return True

    if head[0] == tail[0] - 1 and head[1] == tail[1] - 1:
        return True

    if head[0] == tail[0] + 1 and head[1] == tail[1] + 1:
        return True

    if head[0] == tail[0] - 1 and head[1] == tail[1] + 1:
        return True

    if head[0] == tail[0] + 1 and head[1] == tail[1] - 1:
        return True

    return False


def get_valid_tail_position(head, tail):
    if is_valid_tail_position(head, tail):
        # print("valid")
        return (tail[0], tail[1])

    if tail[0] == head[0]:
        # move sideways
        return (tail[0], tail[1] - 1 if tail[1] > head[1] else tail[1] + 1)
    elif tail[1] == head[1]:
        # move up / down
        return (tail[0] - 1 if tail[0] > head[0] else tail[0] + 1, tail[1])
    else:
        if is_valid_tail_position(head, (tail[0] + 1, tail[1] + 1)):
            return (tail[0] + 1, tail[1] + 1)
        if is_valid_tail_position(head, (tail[0] - 1, tail[1] + 1)):
            return (tail[0] - 1, tail[1] + 1)
        if is_valid_tail_position(head, (tail[0] + 1, tail[1] - 1)):
            return (tail[0] + 1, tail[1] - 1)
        if is_valid_tail_position(head, (tail[0] - 1, tail[1] - 1)):
            return (tail[0] - 1, tail[1] - 1)

    raise Exception("No new position found...")


def move_head(head, direction):
    if direction == "R":
        return (head[0], head[1] + 1)
    if direction == "U":
        return (head[0] + 1, head[1])
    if direction == "L":
        return (head[0], head[1] - 1)
    if direction == "D":
        return (head[0] - 1, head[1])


def navigate_grid(fn):
    with open(fn) as f:
        moves = [l.strip().split() for l in f.readlines()]

        #      (up, right)
        head = (0, 0)
        tail = (0, 0)

        tail_positions = [(tail[0], tail[1])]

        for direction, count in moves:
            for _ in range(int(count)):
                head = move_head(head, direction)

                # move tail to valid position
                tail = get_valid_tail_position(head, tail)
                tail_positions.insert(0, (tail[0], tail[1]))

    return len(set(tail_positions))


if __name__ == "__main__":
    result = navigate_grid("test.txt")
    print(result)
    assert result == 13

    result = navigate_grid("input.txt")
    print(result)
    assert result == 6271
