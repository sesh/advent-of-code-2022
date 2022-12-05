def puzzle_func(fn):
    with open(fn) as f:
        lines = [l for l in f.readlines()]

    return 0


if __name__ == "__main__":
    result = puzzle_func("test.txt")
    assert result == 2

    result = puzzle_func("input.txt")
    print(result)
