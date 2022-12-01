from part01 import load_calorie_counts


if __name__ == "__main__":
    elf_top_three = sorted(load_calorie_counts("data_test.txt"), reverse=True)[:3]
    assert sum(elf_top_three) == 45000

    print(
        "01 - Part 02:",
        sum(sorted(load_calorie_counts("data_01.txt"), reverse=True)[:3]),
    )
