from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Sensor = namedtuple("Sensor", ["sensor", "beacon"])

def gen_point(data):
    coords = data.split('at ')[1].split(', ')
    return Point(int(coords[0][2:]), int(coords[1][2:]))

def gen_sensor(data):
    return Sensor(gen_point(data[0]), gen_point(data[1]))

def calc_manhattan(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def main():
    lines = [l.strip().split(': ') for l in open('../input.txt').readlines()]
    data = list(map(lambda x: gen_sensor(x), lines))
    data2 = [((z := [int(x.split(" ")[y].split("=")[1].strip(",").strip(":")) for y in [2, 3, -2, -1]])[:2], z[2:]) for x in open("../input.txt").read().splitlines()]
    print(f'Silver: {silver(data, 2_000_000)}')
    for x in range(4_000_000):
        if (result := gold(data, x)):
            break
    print(f'Gold: {result}')

def silver(data, target):
    x_ranges = set()
    for sensor, beacon in data:
        manhattan = calc_manhattan(sensor, beacon)
        if (man_y := abs(sensor.y - target)) <= manhattan:
            x_ranges.add((sensor.x - (man_x := manhattan - man_y), sensor.x + man_x))
    total_range = []
    ranges = sorted(x_ranges)
    start, end = ranges[0]
    for x, y in ranges[1:]:
        if x > end:
            total_range.append((start, end))
            start, end = x, y
            continue
        if y > end:
            end = y
    if (start, end) not in total_range:
        total_range.append((start, end))
    return sum(abs(x[1] - x[0]) + 1 for x in total_range) - sum([beacon.y == target for beacon in set(x.beacon for x in data)])

def gold(data, target):
    x_ranges = set()
    for sensor, beacon in data:
        manhattan = calc_manhattan(sensor, beacon)
        if (man_y := abs(sensor.y - target)) <= manhattan:
            x_ranges.add((sensor.x - (man_x := manhattan - man_y), sensor.x + man_x))
    total_range = []
    ranges = sorted(x_ranges)
    start, end = ranges[0]
    for x, y in ranges[1:]:
        if x > end:
            total_range.append((start, end))
            start, end = x, y
            continue
        if y > end:
            end = y
    if (start, end) not in total_range:
        total_range.append((start, end))
    if len(total_range) > 1:
        return (total_range[0][1] + 1) * 4_000_000 + target
    return None

if __name__ == "__main__":
    main()