from part01 import check_pairs


def check_overlap(a, b):
    # https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python
    return list(range(max(a[0], b[0]), min(a[-1], b[-1]) + 1)) != []


if __name__ == "__main__":
    count = check_pairs("data_test.txt", check_overlap)
    assert count == 4

    count = check_pairs("data_01.txt", check_overlap)
    print(count)
