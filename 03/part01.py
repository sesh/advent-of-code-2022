import string


def score_bad_items(fn):
    score = 0
    for l in open(fn).readlines():
        if l:
            sack_one, sack_two = l[: len(l) // 2], l[len(l) // 2 :]
            for c in sack_one:
                if c in sack_two:
                    score += 1 + (
                        string.ascii_lowercase + string.ascii_uppercase
                    ).index(c)
                    break

    return score


if __name__ == "__main__":
    score = score_bad_items("data_test.txt")
    assert score == 157

    score = score_bad_items("data_01.txt")
    print(score)
