from part01 import puzzle_func

if __name__ == "__main__":
    result = puzzle_func("test.txt", 14)
    assert result == 19

    result = puzzle_func("input.txt", 14)
    print(result)
