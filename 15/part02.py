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

        print('creating map')
        map = np.full((max_x + 1, max_y + 1), fill_value='.')
        print('map created')

        for sensor, beacon in sensors:
            if is_in_bounds(sensor, bounds):
                map[sensor[1]][sensor[0]] = 'S'
            if is_in_bounds(beacon, bounds):
                map[beacon[1]][beacon[0]] = 'B'

        # draw_map(map, min_y)
        # print('---')

        for sensor_num, (sensor, beacon) in enumerate(sensors):
            print(f"SENSOR: {sensor_num + 1}/{len(sensors)}")
            dist = manhattan_distance(sensor, beacon)
            x, y = sensor

            if is_in_bounds((x, y), bounds) and map[y][x] == '.':
                map[y][x] = '#'

            for j in range(dist):  # up down
                target_row = y - j
                dist_to_target = abs(y - target_row)
                width = dist - dist_to_target

                for i in range(width):
                    if is_in_bounds((x, target_row), bounds) and map[target_row][x] == '.':
                        map[target_row][x] = '#'

                    if is_in_bounds((x+i+1, target_row), bounds) and map[target_row][x+i+1] == '.':
                        map[target_row][x+i+1] = '#'

                    if is_in_bounds((x-i-1, target_row), bounds) and map[target_row][x-i-1] == '.':
                        map[target_row][x-i-1] = '#'

                target_row = y + j
                dist_to_target = abs(y - target_row)
                width = dist - dist_to_target

                for i in range(width):
                    if is_in_bounds((x, target_row), bounds) and map[target_row][x] == '.':
                        map[target_row][x] = '#'

                    if is_in_bounds((x+i+1, target_row), bounds) and map[target_row][x+i+1] == '.':
                        map[target_row][x+i+1] = '#'

                    if is_in_bounds((x-i-1, target_row), bounds) and map[target_row][x-i-1] == '.':
                        map[target_row][x-i-1] = '#'

        # draw_map(map, min_y)

        # search for the result
        for i, line in enumerate(map):
            if '.' in line:
                result = i + ([x for x in line].index('.') * 4000000)
                print('RESULT:', result)

        return result


if __name__ == "__main__":
    result = puzzle_func("test.txt", 20)
    print(result)
    assert result == 56000011

    result = puzzle_func("input.txt", 4000000)
    print(result)

