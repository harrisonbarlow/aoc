import numpy as np
from copy import deepcopy

sand_pos = (0, 500)

def add_sand(cave, max_y=None):
    y, x = sand_pos

    while True:
        for dy, dx in [(1, 0), (1, -1), (1, 1)]:
            if max_y is not None and y + dy > max_y:
                raise IndexError

            if cave[y + dy, x + dx] == '.':
                y, x = y + dy, x + dx
                break
        else:
            cave[y, x] = 'o'
            break

    return cave


def solve1(cave, max_y):
    index = 0

    while True:
        try:
            cave = add_sand(cave, max_y=max_y)
            index += 1
        except IndexError:
            break

    return index


def solve2(cave):
    index = 0
    y, x = sand_pos

    while cave[y, x] != 'o':
        cave = add_sand(cave)
        index += 1
        
    return index


def main():
    paths = [line.split('->') for line in open('input.txt').read().splitlines()]
    cave = np.full((1000, 1000), '.')
    max_y = 0

    for path in paths:
        for p1, p2 in zip(path, path[1:]):
            p1_x, p1_y = map(int, p1.split(','))
            p2_x, p2_y = map(int, p2.split(','))

            max_y = max(p1_y, p2_y, max_y)

            if p1_x == p2_x:
                cave[min(p1_y, p2_y):max(p1_y, p2_y) + 1, p1_x] = '#'

            if p1_y == p2_y:
                cave[p1_y, min(p1_x, p2_x):max(p1_x, p2_x) + 1] = '#'

    cave[max_y + 2, :] = '#'

    print(solve1(deepcopy(cave), max_y))
    print(solve2(deepcopy(cave)))


if __name__ == "__main__":
    main()