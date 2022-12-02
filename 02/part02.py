from part01 import score_ab


winning_choice_for_b = {"A": "Y", "B": "Z", "C": "X"}
losing_choice_for_b = {"A": "Z", "B": "X", "C": "Y"}
draw_choice_for_b = {"A": "X", "B": "Y", "C": "Z"}


def rps(fn):
    turns = [x.strip().split() for x in open(fn).readlines() if x.strip()]
    score = 0

    for a, b in turns:
        if b == "X":
            b = losing_choice_for_b[a]
        elif b == "Y":
            b = draw_choice_for_b[a]
        else:
            b = winning_choice_for_b[a]

        score += score_ab(a, b)

    return score


if __name__ == "__main__":
    score = rps("data_test.txt")
    assert score == 12

    score = rps("data_02.txt")
    print(score)
