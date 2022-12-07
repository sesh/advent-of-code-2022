from part01 import directory_sizes


def find_smallest_dir(fn):
    dirs = directory_sizes(fn)

    fs_size = 70000000
    required_space = 30000000
    free_space = fs_size - dirs["/"]["size"]
    required_to_delete = required_space - free_space

    return min([d["size"] for d in dirs.values() if d["size"] > required_to_delete])


if __name__ == "__main__":
    result = find_smallest_dir("test.txt")
    assert result == 24933642
    print("---")

    result = find_smallest_dir("input.txt")
    print(result)
