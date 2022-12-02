scores = {"X": 1, "Y": 2, "Z": 3}
draws = [("A", "X"), ("B", "Y"), ("C", "Z")]
losing_for_a = [("A", "Y"), ("B", "Z"), ("C", "X")]
winning_for_a = [("A", "Z"), ("B", "X"), ("C", "Y")]


def score_ab(player_a, player_b):
    score = scores[player_b]

    # score for match
    if (player_a, player_b) in draws:
        score += 3
    # losing hands for A
    elif (player_a, player_b) in losing_for_a:
        score += 6
    # winning for A
    elif (player_a, player_b) in winning_for_a:
        score += 0
    else:
        print(player_a, player_b)
        print("OH NO")

    return score


def rps(fn):
    turns = [x.strip().split() for x in open(fn).readlines() if x.strip()]

    score = 0
    for player_a, player_b in turns:
        score += score_ab(player_a, player_b)

    return score


if __name__ == "__main__":
    score = rps("data_test.txt")
    assert score == 15

    score = rps("data_02.txt")
    print(score)
