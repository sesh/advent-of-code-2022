from part01 import xy_from_string, draw_map, manhattan_distance
import numpy as np


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
            overlaps = []
            for sensor, beacon in sensors:
                dist = manhattan_distance(sensor, beacon)
                if sensor[1] < target_row and sensor[1] + dist > target_row:
                    overlaps.append((sensor, beacon, dist))
                if sensor[1] > target_row and sensor[1] - dist < target_row:
                    overlaps.append((sensor, beacon, dist))

            line = ['.' for x in range(min_x, max_x + 1)]
            for sensor, beacon, dist in overlaps:
                x, y = sensor
                x = x - min_x

                if is_in_bounds(sensor, bounds) and sensor[1] == target_row:
                    line[sensor[1]] == 'S'
                if is_in_bounds(beacon, bounds) and beacon[1] == target_row:
                    line[beacon[0]] = 'B'

                print(line)

if __name__ == "__main__":
    result = puzzle_func("test.txt", 20)
    print(result)
    assert result == 56000011

    result = puzzle_func("input.txt", 4000000)
    print(result)

