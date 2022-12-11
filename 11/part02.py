from part01 import puzzle_func


if __name__ == "__main__":
    result = puzzle_func("test.txt", 10000, use_relief=False)
    print(result)
    assert result == 2713310158

    result = puzzle_func("input.txt", 10000, use_relief=False)
    print(result)
