def check_contains(a, b):

    return (min(a) >= min(b) and max(a) <= max(b)) or (  # a in b
        min(b) >= min(a) and max(b) <= max(a)
    )  # b in a


def check_pairs(fn, func):
    count = 0
    with open(fn) as f:
        for l in f.readlines():
            a, b = l.split(",")
            a = [int(x) for x in a.split("-")]
            b = [int(x) for x in b.split("-")]
            if func(a, b):
                count += 1
    return count


if __name__ == "__main__":
    count = check_pairs("data_test.txt", check_contains)
    assert count == 2

    count = check_pairs("data_01.txt", check_contains)
    print(count)
