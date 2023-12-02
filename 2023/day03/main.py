import re

from string import punctuation
from collections import defaultdict
from functools import reduce
from operator import mul

def get_number(line, x):
    for number in re.finditer(r'\b\d+', line):
        if number.start() <= x < number.end():
            return int(number.group())

    return None


def solve2(lines):
    gears = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '*':
                gear = set()
                for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < len(line) and 0 <= ny < len(lines):
                        if lines[ny][nx].isdigit():
                            gear.add(get_number(lines[ny], nx))

                gears.append(gear)

    return sum([
        reduce(mul, gear)
        for gear in gears
        if len(gear) == 2
    ])


def solve1(lines):
    parts = []
    positions = defaultdict(set)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.' and char in punctuation:
                for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < len(line) and 0 <= ny < len(lines):
                        if lines[ny][nx].isdigit():
                            positions[ny].add(nx)


    for y, line in enumerate(lines):
        for number in re.finditer(r'\b\d+', line):
            if any(position in positions[y] for position in range(*number.span())):
                parts.append(int(number.group()))

    return sum(parts)


def main():
    lines = [line.rstrip() for line in open('input.txt')]

    print(solve1(lines))
    print(solve2(lines))


if __name__ == '__main__':
    main()