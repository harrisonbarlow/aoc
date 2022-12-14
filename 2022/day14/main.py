import numpy as np
from copy import deepcopy

sand_pos = (0, 500)

def add_sand(cave, max_y=None):
    (y, x) = sand_pos
    cave[y, x] = 'o'

    while True:
        for (dy, dx) in [(1, 0), (1, -1), (1, 1)]:
            if max_y is not None and y+dy > max_y:
                raise IndexError

            if cave[y+dy, x+dx] == '.':
                cave[y+dy, x+dx] = 'o'
                cave[y, x] = '.'

                (y, x) = (y+dy, x+dx)

                break
        else:
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
    (y, x) = sand_pos

    while True:
        index += 1
        cave = add_sand(cave)

        if cave[y, x] == 'o':
            break
        
    return index


def main():
    input = [line.split('->') for line in open('input.txt').read().splitlines()]

    cave = np.full((1000, 1000), '.')

    max_y = 0

    for path in input:
        for start, end in zip(path, path[1:]):
            start_x, start_y = map(int, start.split(','))
            end_x, end_y = map(int, end.split(','))

            if start_y > max_y or end_y > max_y:
                max_y = max(start_y, end_y)

            if start_x == end_x:
                cave[min(start_y, end_y):max(start_y, end_y) + 1, start_x] = '#'

            if start_y == end_y:
                cave[start_y, min(start_x, end_x):max(start_x, end_x) + 1,] = '#'


    cave[max_y + 2, :] = '#'

    print(solve1(deepcopy(cave), max_y))
    print(solve2(deepcopy(cave)))


if __name__ == "__main__":
    main()