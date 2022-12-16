from part01 import xy_from_string, draw_map, manhattan_distance
import multiprocessing.dummy as mp


def is_in_bounds(point, bounds):
    x, y = point

    if x < bounds[0]:
        return False
    if y < bounds[1]:
        return False
    if x > bounds[2]:
        return False
    if y > bounds[3]:
        return False

    return True


def check_row(target_row, sensors, bounds, min_x, max_x, max_y):
    print(f"{target_row}/{max_y}")
    start_end_points = []
    for sensor, beacon in sensors:
        dist = manhattan_distance(sensor, beacon)
        x, y = sensor
        x = x - min_x

        dist_to_target = abs(y - target_row)
        width = dist - dist_to_target

        if width > 0:
            # if there are multiple starts that start with 0, then we need to choose the one with max_length
            start = max([0, x - width])
            end = min([x + width, max_x])
            start_end_points.append((start, end, width))

    # determine if there are any gaps
    zero_start_points = [x for x in start_end_points if x[0] == 0]
    if len(zero_start_points) > 1:
        zero_start_points.sort(key=lambda x: x[1], reverse=True)
        # print(zero_start_points)
        for zsp in zero_start_points[1:]:
            start_end_points.remove(zsp)

    max_end_points = [x for x in start_end_points if x[1] == max_y]
    if len(max_end_points) > 1:
        max_end_points.sort(key=lambda x: x[0])

        for mep in max_end_points[1:]:
            start_end_points.remove(mep)

    start_end_points.sort(key=lambda x: x[0])

    # eliminate any points that overlap
    points = []
    for a_start, a_end, a_length in start_end_points:
        overlap = False

        for b_start, b_end, b_length in start_end_points:
            # check if a is inside b, set overlap to true
            if a_start == b_start and a_end == b_end:
                continue

            elif a_start >= b_start and a_end <= b_end:
                overlap = True
                break

        if not overlap:
            points.append((a_start, a_end, a_length))

    start_end_points = points

    if not start_end_points:
        return None

    # calculate running total
    running_total = min_x - start_end_points[0][0]
    max_end = start_end_points[-1][1]

    for i, (start, end, _) in enumerate(start_end_points):
        if i + 1 < len(start_end_points):
            next_start, next_end, next_len = start_end_points[i + 1]
            if next_start - end > 0:
                running_total += next_start - end

        if end > max_end:
            max_end = end

    running_total += max_x - max_end

    # if running_total > 0 then we are on the right line
    if running_total > 0:
        line = ["." for x in range(min_x, max_x + 1)]

        for start, end, length in start_end_points:
            for i in range(start, end + 1):
                line[i] = "#"

        if "." in line:
            return target_row + (4000000 * line.index("."))


def puzzle_func(fn, max_xy=10):
    results = []

    with open(fn) as f:
        lines = [l.strip() for l in f.readlines()]
        sensors = []
        flat_list_of_coords = []

        for l in lines:
            sensor, beacon = l.split(": ")
            sensors.append((xy_from_string(sensor), xy_from_string(beacon)))

        min_x = 0
        min_y = 0
        max_x = max_xy
        max_y = max_xy
        bounds = (min_x, min_y, max_x, max_y)

        for target_row in range(min_y, max_y + 1):
            result = check_row(target_row, sensors, bounds, min_x, max_x, max_y)
            if result:
                results.append(result)

    if len(results) == 1:
        return results[0]
    else:
        return 0


if __name__ == "__main__":
    result = puzzle_func("test.txt", 20)
    assert result == 56000011

    result = puzzle_func("input.txt", 4000000)
    assert result > 5178564295828
    print(result)
