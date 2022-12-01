def load_calorie_counts(fn):
    parts = open(fn, "r").read().split("\n\n")
    return [sum([int(l) for l in elf.split() if l.strip()]) for elf in parts]


if __name__ == "__main__":
    elf_calorie_totals = load_calorie_counts("data_test.txt")
    assert elf_calorie_totals == [6000, 4000, 11000, 24000, 10000]

    elf_calorie_totals = load_calorie_counts("data_01.txt")
    print("01 - Part 01:", max(elf_calorie_totals))
