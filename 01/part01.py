def load_calorie_counts(fn):
    elf_totals = []

    with open(fn, "r") as f:
        elf = []

        for l in f.readlines() + ["\n"]:
            l = l.strip()
            if not l:
                elf_totals.append(sum(elf))
                elf = []
            else:
                elf.append(int(l))

    return elf_totals


if __name__ == "__main__":
    elf_calorie_totals = load_calorie_counts("data_test.txt")
    assert elf_calorie_totals == [6000, 4000, 11000, 24000, 10000]

    elf_calorie_totals = load_calorie_counts("data_01.txt")
    print("01 - Part 01:", max(elf_calorie_totals))
