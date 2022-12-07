import re


def directory_sizes(fn):
    with open(fn) as f:
        lines = [l for l in f.readlines()]

        dirs = {}
        current_dir = ""
        max_depth = 1

        for l in lines:
            if l.startswith("$ cd"):
                if ".." in l:
                    current_dir = "/".join(current_dir.split("/")[:-1])
                else:
                    # lol, where is that coming from?
                    current_dir = (
                        current_dir + "/" + l.split("$ cd")[-1].strip()
                    ).replace("//", "/")
                    if current_dir not in dirs:
                        dirs[current_dir] = {"size": 0, "dirs": []}

                max_depth = max([current_dir.count("/"), max_depth])
            elif l.startswith("$ ls"):
                pass
            elif l.startswith("dir"):
                dirs[current_dir]["dirs"].append(
                    (current_dir + "/" + l.split("dir")[-1].strip()).replace("//", "/")
                )
            else:
                size, name = l.split(" ")
                dirs[current_dir]["size"] += int(size)

        # expand sub-directories
        while max_depth > 0:
            for directory in dirs.values():
                for subdir in directory["dirs"]:
                    if subdir.count("/") == max_depth:
                        directory["size"] += dirs[subdir]["size"]
            max_depth -= 1

        return dirs


def total_size_under_x(fn, x):
    dirs = directory_sizes(fn)

    size = 0
    for name, d in dirs.items():
        if d["size"] <= x:
            size += d["size"]

    return size


if __name__ == "__main__":
    result = total_size_under_x("test.txt", 100000)
    assert result == 95437

    result = total_size_under_x("input.txt", 100000)
    print(result)
