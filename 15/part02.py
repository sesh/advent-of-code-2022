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
    line = ['.' for x in range(min_x, max_x + 1)]

    for sensor, beacon in sensors:
        dist = manhattan_distance(sensor, beacon)
        x, y = sensor
        x = x - min_x

        if is_in_bounds(sensor, bounds) and sensor[1] == target_row:
            line[sensor[0]] = 'S'
        if is_in_bounds(beacon, bounds) and beacon[1] == target_row:
            line[beacon[0]] = 'B'

        dist_to_target = abs(y - target_row)
        width = dist - dist_to_target

        for i in range(width):
            if is_in_bounds((x, target_row), bounds):
                line[x] = '#'
            if is_in_bounds((x+i+1, target_row), bounds):
                line[x+i+1] = '#'
            if is_in_bounds((x-i-1, target_row), bounds):
                line[x-i-1] = '#'


    if "." in line:
        print(target_row + (4000000 * line.index(".")))
        return target_row + (4000000 * line.index("."))


def puzzle_func(fn, max_xy=10):
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
                return result


if __name__ == "__main__":
    result = puzzle_func("test.txt", 20)
    print(result)
    assert result == 56000011

    result = puzzle_func("input.txt", 4000000)
    print(result)

