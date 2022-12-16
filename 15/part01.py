def xy_from_string(s):
    x = None
    y = None

    s = s.replace(",", "")
    parts = s.split()

    for p in parts:
        if p.startswith("x="):
            x = int(p[2:])
        elif p.startswith("y="):
            y = int(p[2:])

    return x, y


def get_bounds_from_coords(coords):
    min_x, min_y, max_x, max_y = None, None, None, None
    for x, y in coords:
        if min_x == None or min_x > x:
            min_x = x
        if max_x == None or max_x < x:
            max_x = x

        if min_y == None or min_y > y:
            min_y = y
        if max_y == None or max_y < y:
            max_y = y

    return min_x, min_y, max_x, max_y


def draw_map(map, min_y):
    i = min_y
    for line in map:
        print(i, "".join(line))
        i += 1


def manhattan_distance(point1, point2):
    distance = 0
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance


def puzzle_func(fn, target_row=10):
    with open(fn) as f:
        lines = [l.strip() for l in f.readlines()]
        sensors = []
        flat_list_of_coords = []

        for l in lines:
            sensor, beacon = l.split(": ")
            sensors.append((xy_from_string(sensor), xy_from_string(beacon)))
            flat_list_of_coords.append(xy_from_string(sensor))
            flat_list_of_coords.append(xy_from_string(beacon))

        min_x, min_y, max_x, max_y = get_bounds_from_coords(flat_list_of_coords)

        overlaps = []
        for sensor, beacon in sensors:
            dist = manhattan_distance(sensor, beacon)
            if sensor[1] < target_row and sensor[1] + dist > target_row:
                overlaps.append((sensor, beacon, dist))
            if sensor[1] > target_row and sensor[1] - dist < target_row:
                overlaps.append((sensor, beacon, dist))

        line = ["." for x in range(min_x, max_x + 1)]
        max_left = 0

        for sensor, beacon, dist in overlaps:
            x, y = sensor
            x = x - min_x

            if beacon[1] == target_row:
                line[beacon[0]] = "B"

            dist_to_target = abs(y - target_row)
            width = dist - dist_to_target

            if line[x] != "B":
                line[x] = "#"

            for i in range(width):
                try:
                    if line[x + i + 1] != "B":
                        line[x + i + 1] = "#"
                except:
                    line.append("#")

                if x - i - 1 < 0 and x - i - 1 < max_left:
                    max_left = x - i - 1
                else:
                    if line[x - i - 1] != "B":
                        line[x - i - 1] = "#"

        return line.count("#") + abs(max_left)


if __name__ == "__main__":
    result = puzzle_func("test.txt")
    assert result == 26

    result = puzzle_func("input.txt", 2000000)
    assert result != 4293821
    assert result > 4181485
    assert result == 5181556

    print(result)
