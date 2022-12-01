from part01 import load_calorie_counts


def get_top_three(totals):
    return sorted(totals, reverse=True)[:3]


if __name__ == "__main__":
    elf_top_three = get_top_three(load_calorie_counts("data_test.txt"))
    assert sum(elf_top_three) == 45000

    elf_top_three = get_top_three(load_calorie_counts("data_01.txt"))
    print("01 - Part 02:", sum(elf_top_three))
