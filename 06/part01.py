def puzzle_func(fn, marker_len):
    with open(fn) as f:
        datastream = f.read().strip()

        for i in range(len(datastream)):
            for j, ch in enumerate(datastream[i : i + marker_len]):
                if datastream[i : i + marker_len].count(ch) > 1:
                    break
                if j == len(datastream[i : i + marker_len]) - 1:
                    return i + marker_len

    return 0


if __name__ == "__main__":
    result = puzzle_func("test.txt", 4)
    assert result == 7

    result = puzzle_func("input.txt", 4)
    print("1:", result)

    result = puzzle_func("test.txt", 14)
    assert result == 19

    result = puzzle_func("input.txt", 14)
    print("2:", result)
