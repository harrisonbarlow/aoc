import re
from collections import namedtuple

Point = namedtuple("Point", "x y")


def manhattan_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def get_edge(position, distance):
    points = []

    for dy in range(-distance, distance + 1):
        ax = distance - abs(dy)

        for dx in (-ax, ax):
            points.append(Point(position.x + dx, position.y + dy))

    return points


def solve1(sensors, beacons, row):
    coverage = set()

    for sensor, beacon in zip(sensors, beacons):
        distance = manhattan_distance(sensor, beacon)

        for dy in range(-distance, distance + 1):
            if sensor.y + dy == row:
                for dx in range(-distance, distance + 1):
                    if abs(dy) + abs(dx) <= distance:
                        c = (sensor.x + dx, sensor.y + dy)
                        coverage.add(c)

    return len(coverage - set(beacons))


def solve2(sensors, beacons, limit):
    points = []
    distances = {}

    for sensor, beacon in zip(sensors, beacons):
        distance = manhattan_distance(sensor, beacon)
        distances[sensor] = distance

        edge = get_edge(sensor, distance + 1)
        points.extend(edge)

    for point in points:
        if 0 < point.x < limit and 0 < point.y < limit:
            for sensor in distances:
                distance = manhattan_distance(point, sensor)

                if distance <= distances[sensor]:
                    break
            else:
                return point.x * 4000000 + point.y


def main():
    sensors, beacons = [], []
    for line in open('input.txt').read().splitlines():
        sx, sy, bx, by = map(int, re.findall('(-?\d+)', line))

        sensors.append(Point(sx, sy))
        beacons.append(Point(bx, by))

    print(solve1(sensors, beacons, 2000000))
    print(solve2(sensors, beacons, 4000000))


if __name__ == "__main__":
    main()