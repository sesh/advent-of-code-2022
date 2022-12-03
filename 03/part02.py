import string


def score_badges(fn):
    score = 0
    sacks = [x.strip() for x in open(fn).readlines() if x.strip()]

    for a, b, c in [sacks[i : i + 3] for i in range(0, len(sacks), 3)]:
        for ch in a:
            if ch in b and ch in c:
                score += 1 + (string.ascii_lowercase + string.ascii_uppercase).index(ch)
                break

    return score


if __name__ == "__main__":
    score = score_badges("data_test.txt")
    assert score == 70

    score = score_badges("data_01.txt")
    print(score)
