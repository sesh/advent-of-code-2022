import json


def compare(left, right):
    if type(left) == int and type(right) == list:
        left = [left]
    if type(right) == int and type(left) == list:
        right = [right]

    if type(left) == int and type(right) == int:
        # If both values are integers, the lower integer should come first.
        # If the left integer is lower than the right integer, the inputs are in the right order.
        # If the left integer is higher than the right integer, the inputs are not in the right order.
        # Otherwise, the inputs are the same integer; continue checking the next part of the input.
        if left < right:
            return True
        if left > right:
            return False
    else:
        # If both values are lists, compare the first value of each list, then the second value, and so on.
        # If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
        for i, l in enumerate(left):
            # If the right list runs out of items first, the inputs are not in the right order.
            try:
                r = right[i]
            except IndexError:
                return False

            result = compare(l, r)
            if result != None:
                return result

        # If the left list runs out of items first, the inputs are in the right order.
        if len(left) < len(right):
            return True


def find_ordered_pairs(fn):
    with open(fn) as f:
        pairs = [
            [json.loads(y) for y in x.splitlines()] for x in f.read().split("\n\n")
        ]

        correctly_ordered = []

    for i, (left, right) in enumerate(pairs):
        if compare(left, right):
            correctly_ordered.append(i + 1)

    return sum(correctly_ordered)


if __name__ == "__main__":
    result = find_ordered_pairs("test.txt")
    print(result)
    assert result == 13

    result = find_ordered_pairs("input.txt")
    print(result)
