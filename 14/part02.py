from part01 import puzzle_func


if __name__ == "__main__":
    result = puzzle_func("test.txt", add_floor=True)
    assert result == 93

    result = puzzle_func("input.txt", add_floor=True)
    print(result)
